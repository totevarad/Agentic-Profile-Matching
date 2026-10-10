import json
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

from state import AgentState
from tools import extract_requirements, rag_search, compare_candidates, vectorstore
from agent_logger import (
    logger,
    log_user_prompt,
    log_agent_action,
    log_agent_reasoning,
    timed_llm_invoke,
)

load_dotenv()
try:
    llm = ChatOpenAI(
        model="apodex/apodex-1.1-mini:free", 
        temperature=0.2,
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )
except Exception as e:
    logger.warning(f"Could not initialize OpenRouter in matching_agent: {e}")
    llm = None

def parse_jd_node(state: AgentState):
    jd = state.get("job_description", "")
    log_agent_action("Executing node: parse_jd_node", details=f"Parsing raw JD (length: {len(jd)} chars)")
    print(f"[Node: parse_jd_node] Parsing JD (length: {len(jd)})")
    return {"job_description": jd.strip()}

def extract_requirements_node(state: AgentState):
    jd = state.get("job_description", "")
    log_agent_action("Executing node: extract_requirements_node", details="Starting requirements extraction")
    print("[Node: extract_requirements_node] Extracting requirements...")
    
    # Only append user feedback if this was explicitly an adjust_requirements intent
    feedback = state.get("feedback", "")
    if feedback == "adjust_requirements":
        hist = state.get("conversation_history", [])
        if hist and hist[-1].get("role") == "user":
            user_msg = hist[-1].get("content", "")
            log_user_prompt(user_msg, context="Additional user requirement feedback")
            jd = jd + f"\n\nAdditional Requirements from user: {user_msg}"
            log_agent_action("Appended user feedback to Job Description for re-extraction")
        
    req_json_str = extract_requirements.invoke({"jd": jd})
    try:
        req_dict = json.loads(req_json_str)
    except Exception as e:
        log_agent_action("Failed parsing requirements JSON, using empty fallback", details=str(e))
        req_dict = {"must_have_skills": [], "nice_to_have_skills": []}

    log_agent_reasoning(
        "Extracted Job Requirements",
        f"Must-have: {req_dict.get('must_have_skills', [])} | Nice-to-have: {req_dict.get('nice_to_have_skills', [])} | Experience: {req_dict.get('experience_years', 0)} years"
    )
            
    return {"job_requirements": req_dict, "job_description": jd}

def search_resumes_node(state: AgentState):
    reqs = state.get("job_requirements", {})
    log_agent_action("Executing node: search_resumes_node", details="Searching resumes based on requirements")
    print("[Node: search_resumes_node] Searching resumes based on requirements...")
    query = f"Must have: {', '.join(reqs.get('must_have_skills', []))} Nice to have: {', '.join(reqs.get('nice_to_have_skills', []))}"
    log_agent_action("Executing resume RAG search with query", details=query)
    candidates_json_str = rag_search.invoke({"query": query})
    try:
        candidates_list = json.loads(candidates_json_str)
    except Exception as e:
        log_agent_action("Failed parsing candidates list JSON", details=str(e))
        candidates_list = []
    log_agent_action("Candidate shortlist retrieved", details=f"Retrieved {len(candidates_list)} candidates")
    return {"candidate_shortlist": candidates_list}

def multi_round_screening_node(state: AgentState):
    candidates = state.get("candidate_shortlist", [])
    reqs = state.get("job_requirements", {})
    min_exp = reqs.get("experience_years", 0)
    must_haves = reqs.get("must_have_skills", [])
    log_agent_action("Executing node: multi_round_screening_node", details=f"Screening candidate pool ({len(candidates)} total)")
    print("[Node: multi_round_screening_node] Starting multi-round screening...")
    
    candidates = sorted(candidates, key=lambda x: x.get("score", 0), reverse=True)
    top_candidates = candidates[:5] # Analyze top 5 for speed
    log_agent_action(f"Screening round 1: Selected top {len(top_candidates)} candidates by similarity score")
    
    reasoning = {}
    decisions = {}
    if llm:
        for cand in top_candidates:
            cand_exp = cand.get("experience", 0)
            cand_skills = cand.get("skills", "")
            score = cand.get("score", 0)
            prompt = f"""
            Candidate: {cand['name']}
            Skills: {cand_skills}
            Experience: {cand_exp} years
            Vector Similarity Score: {score}

            Role Requirements:
            - Must-Have Skills: {must_haves}
            - Minimum Experience: {min_exp} years

            Evaluate this candidate for the role:
            1. Decision: Choose exactly one of 'Hire' or 'No-Hire'.
               - Assign 'Hire' if the candidate has the core must-have skills AND meets or exceeds the required years of experience.
               - Assign 'No-Hire' if the candidate is missing must-have skills OR does not meet the minimum required years of experience.
            2. Reasoning: A concise 1-2 sentence explanation of why they are a match or where they fall short.

            Format your response exactly as:
            Decision: [Hire or No-Hire]
            Reasoning: [Explanation]
            """
            try:
                _, duration, content_str = timed_llm_invoke(
                    llm,
                    prompt,
                    task_name=f"Candidate Screening: {cand['name']} ({cand['candidate_id']})",
                    extract_reasoning=True
                )
                
                # Parse Decision and Reasoning from LLM output
                lines = content_str.strip().split("\n")
                cand_decision = "No-Hire"
                cand_reason = content_str.strip()
                for line in lines:
                    line_clean = line.strip()
                    if line_clean.lower().startswith("decision:"):
                        val = line_clean.split(":", 1)[1].strip().lower()
                        cand_decision = "Hire" if "hire" in val and "no" not in val else "No-Hire"
                    elif line_clean.lower().startswith("reasoning:"):
                        cand_reason = line_clean.split(":", 1)[1].strip()

                decisions[cand["candidate_id"]] = cand_decision
                reasoning[cand["candidate_id"]] = cand_reason
            except Exception as e:
                # Rule-based fallback if LLM call encounters error
                has_skills = any(m.lower() in cand_skills.lower() for m in must_haves) if must_haves else True
                has_exp = cand_exp >= min_exp
                cand_decision = "Hire" if (has_skills and has_exp) else "No-Hire"
                decisions[cand["candidate_id"]] = cand_decision
                fallback_reason = f"Profile evaluated based on skills and {cand_exp} years of experience."
                reasoning[cand["candidate_id"]] = fallback_reason
                log_agent_reasoning(f"Candidate Screening Fallback ({cand['name']})", fallback_reason, details=str(e))
    else:
        for cand in top_candidates:
            cand_exp = cand.get("experience", 0)
            cand_skills = cand.get("skills", "")
            has_skills = any(m.lower() in cand_skills.lower() for m in must_haves) if must_haves else True
            has_exp = cand_exp >= min_exp
            cand_decision = "Hire" if (has_skills and has_exp) else "No-Hire"
            decisions[cand["candidate_id"]] = cand_decision
            reasoning[cand["candidate_id"]] = f"Profile evaluated with {cand_exp} years experience."
            
    for cand in top_candidates:
        cid = cand["candidate_id"]
        cand["decision"] = decisions.get(cid, "No-Hire")
        score = cand.get("score", 0)
        log_agent_reasoning(
            f"Candidate Decision: {cand['name']}",
            f"Status: {cand['decision']} | Rationale: {reasoning.get(cid, '')}"
        )
        log_agent_action(f"Assigned decision for candidate {cand['name']}", details={"decision": cand["decision"], "score": score})
        
    log_agent_action("Multi-round screening phase completed", details=f"Screened {len(top_candidates)} candidates")
    return {"candidate_shortlist": top_candidates, "candidate_reasoning": reasoning, "current_phase": "ScreeningComplete"}

def generate_report_node(state: AgentState):
    top_candidates = state.get("candidate_shortlist", [])
    reasoning = state.get("candidate_reasoning", {})
    log_agent_action("Executing node: generate_report_node", details=f"Compiling match report for {len(top_candidates)} candidates")
    print("[Node: generate_report_node] Generating match report...")
    
    if not top_candidates:
        report = "No candidates found matching the criteria in the resume database."
        log_agent_action("Candidate match report generated (No candidates found)")
        return {"conversation_history": [{"role": "assistant", "content": report}], "feedback": "report_generated"}

    report = "### Candidate Match Report\n\n"
    for cand in top_candidates:
        cid = cand["candidate_id"]
        report += f"**{cand['name']}** ({cand['decision']})\n"
        report += f"- Score: {cand.get('score')}\n"
        report += f"- Reasoning: {reasoning.get(cid, 'No reasoning provided.')}\n\n"
        
    log_agent_action("Candidate Match Report successfully compiled and appended to history")
    return {"conversation_history": [{"role": "assistant", "content": report}], "feedback": "report_generated"}

def human_interaction_node(state: AgentState):
    log_agent_action("Executing node: human_interaction_node", details="Processing conversational input")
    print("[Node: human_interaction_node] Processing user input...")
    history = state.get("conversation_history", [])
    if not history: 
        log_agent_action("No conversation history found in state")
        return {"feedback": "none"}
        
    last_msg = history[-1]["content"]
    log_user_prompt(last_msg, context="Human interaction turn")
    
    if not llm:
        log_agent_action("LLM not initialized, defaulting intent to 'general_query'")
        return {"feedback": "general_query"}

    active_jd = state.get("job_description", "")[:120]
    prompt = f"""
    You are an HR recruitment AI assistant evaluating a user's message in an ongoing session.
    Active Job Description context: "{active_jd}..."
    User Message: "{last_msg}"

    Classify the user's intent into EXACTLY ONE of the following 5 categories:
    1. new_search - The user is requesting to find or search for candidates for a DIFFERENT role, new skill set, or fresh job criteria (e.g. "Find me backend developers...", "Search for frontend developers", "Find candidates who know Python and AWS", "Find me machine learning engineers").
    2. database_query - The user is asking an exploratory question about what exists in the overall resume database (e.g. "Is there any candidate who has less than 3 years of experience and is a UI/UX or frontend developer?", "Do we have any Golang engineers in our database?", "Who has the most years of experience in the database?", "List candidates with backend skills").
    3. compare_candidates - The user wants to compare specific candidates, asks why one candidate scored higher than another, or asks for a head-to-head evaluation (e.g. "Why does Julia Zhang have a higher score than Xavier?", "Compare Julia and David", "Compare the top candidates").
    4. adjust_requirements - The user wants to tweak or add/remove specific criteria from the CURRENT job search (e.g. "Actually, make React a must-have", "Lower the required experience to 2 years", "Also add Docker to must-have").
    5. general_query - General questions about the current shortlist, hiring advice, or greetings.

    Return ONLY the category name: new_search, database_query, compare_candidates, adjust_requirements, or general_query.
    """
    try:
        _, duration, content_str = timed_llm_invoke(
            llm,
            prompt,
            task_name="Intent Classification",
            extract_reasoning=False
        )
        intent = content_str.strip().lower()
        log_agent_reasoning("Intent Classification", f"Categorized user query '{last_msg}' as intent '{intent}'")
        
        # Check for new_search
        if "new_search" in intent or ("search" in intent and "adjust" not in intent and "database" not in intent):
            log_agent_action("Classified user intent", details="new_search")
            return {
                "feedback": "new_search",
                "job_description": last_msg,
                "job_requirements": {},
                "candidate_shortlist": [],
                "candidate_reasoning": {},
                "current_phase": "InitialScreen"
            }
        elif "database" in intent:
            log_agent_action("Classified user intent", details="database_query")
            return {"feedback": "database_query"}
        elif "compare" in intent: 
            log_agent_action("Classified user intent", details="compare_candidates")
            return {"feedback": "compare_candidates"}
        elif "adjust" in intent: 
            log_agent_action("Classified user intent", details="adjust_requirements")
            return {"feedback": "adjust_requirements"}
        else:
            log_agent_action("Classified user intent", details="general_query")
            return {"feedback": "general_query"}
    except Exception as e:
        log_agent_action("Intent classification failed, falling back to general_query", details=str(e))
        return {"feedback": "general_query"}

def tool_execution_node(state: AgentState):
    feedback = state.get("feedback", "")
    log_agent_action("Executing node: tool_execution_node", details=f"Handling feedback type: '{feedback}'")
    print("[Node: tool_execution_node] Executing requested tool...")
    history = state.get("conversation_history", [])
    last_msg = history[-1]["content"] if history else ""
    
    if feedback == "compare_candidates":
        shortlist = state.get("candidate_shortlist", [])
        last_msg_lower = last_msg.lower()
        
        # 1. Identify candidates mentioned specifically in the user prompt
        matched_cands = []
        for cand in shortlist:
            c_name = cand.get("name", "").replace("_", " ").lower()
            c_id = cand.get("candidate_id", "").lower()
            name_tokens = c_name.split()
            # Match full name, ID, or individual name parts (e.g. "julia", "xavier")
            if c_name in last_msg_lower or c_id in last_msg_lower or any(tok in last_msg_lower for tok in name_tokens if len(tok) > 2):
                if cand not in matched_cands:
                    matched_cands.append(cand)
                    
        # 2. If fewer than 2 candidates matched by name, fill with top shortlisted candidates
        if len(matched_cands) < 2:
            for cand in shortlist:
                if cand not in matched_cands:
                    matched_cands.append(cand)
                if len(matched_cands) == 2:
                    break
                    
        # 3. Format detailed real candidate data for comparison
        comparison_data_lines = []
        reasoning_map = state.get("candidate_reasoning", {})
        for c in matched_cands:
            cid = c.get("candidate_id", "")
            c_reason = reasoning_map.get(cid, "No detailed reasoning recorded.")
            comparison_data_lines.append(
                f"- **{c.get('name')}** (ID: `{cid}`)\n"
                f"  - Score: {c.get('score', 'N/A')} | Decision: {c.get('decision', 'N/A')}\n"
                f"  - Years of Experience: {c.get('experience', 0)}\n"
                f"  - Skills: {c.get('skills', 'N/A')}\n"
                f"  - Screening Reasoning: {c_reason}"
            )
            
        cands_text = "\n\n".join(comparison_data_lines)
        cand_names = [c["name"] for c in matched_cands]
        log_agent_action("Executing compare_candidates with factual profiles", details=cand_names)
        
        prompt = f"""
        You are an expert HR recruitment specialist.
        The user asked: "{last_msg}"

        Here are the factual candidate profiles to compare based on their actual screening data:
        {cands_text}

        Active Job Requirements:
        {json.dumps(state.get("job_requirements", {}), indent=2)}

        Please provide an objective, high-quality candidate comparison:
        1. Directly address the user's question (e.g. explain why one candidate has a higher score or why they were evaluated differently).
        2. Present a clear Markdown comparison table detailing their skills, experience, score, and decision.
        3. Conclude with a clear recommendation based on the team's needs.
        Base your answer strictly on the actual candidate data provided above.
        """
        _, duration, content_str = timed_llm_invoke(
            llm,
            prompt,
            task_name=f"Candidate Comparison ({', '.join(cand_names)})",
            extract_reasoning=True
        )
        return {"conversation_history": [{"role": "assistant", "content": content_str}]}

    elif feedback == "database_query":
        log_agent_action("Executing database_query across full candidate pool", details=last_msg)
        # Search the entire Chroma resume database for the query
        db_candidates_str = rag_search.invoke({"query": last_msg})
        try:
            db_candidates = json.loads(db_candidates_str)
        except Exception:
            db_candidates = []
            
        prompt = f"""
        You are an expert recruitment assistant with direct access to the full candidate resume database.
        The user asked: "{last_msg}"

        Relevant candidates retrieved from the entire database matching this query:
        {json.dumps(db_candidates, indent=2)}

        Active Job Requirements in session:
        {json.dumps(state.get("job_requirements", {}), indent=2)}

        Provide a direct, helpful, and factually accurate answer:
        - If the user asks whether any candidates exist with specific criteria (e.g. experience less than 3 years and UI/UX or frontend development), inspect the retrieved candidates' exact experience and skills. List any that match, detailing their years of experience and specific skills.
        - If matching candidates are found, highlight them clearly with bullet points.
        - If none match the user's exact constraints, explicitly state that and explain what candidates were found.
        """
        _, duration, content_str = timed_llm_invoke(
            llm,
            prompt,
            task_name="Database Query Response Generation",
            extract_reasoning=True
        )
        return {"conversation_history": [{"role": "assistant", "content": content_str}]}

    else:
        # general_query
        if not llm:
            msg = "I am unable to process general queries without an LLM configured."
            log_agent_action("LLM not configured for general query response")
            return {"conversation_history": [{"role": "assistant", "content": msg}]}
            
        cands = state.get("candidate_shortlist", [])
        context = f"Shortlisted candidates: {json.dumps(cands)}"
        sys_msg = "You are a helpful HR assistant. Answer the user's query."
        prompt = f"{sys_msg}\n\nContext:\n{context}\n\nUser Query: {last_msg}"
        log_user_prompt(last_msg, context="General query prompt to LLM")
        try:
            _, duration, content_str = timed_llm_invoke(
                llm,
                prompt,
                task_name="General Query Response Generation",
                extract_reasoning=True
            )
            log_agent_action("Generated LLM response for general query", details=f"Response length: {len(content_str)} chars")
            return {"conversation_history": [{"role": "assistant", "content": content_str}]}
        except Exception as e:
            err_msg = f"Error answering query: {e}"
            log_agent_action("Error generating general query response", details=str(e))
            return {"conversation_history": [{"role": "assistant", "content": err_msg}]}

def start_router(state: AgentState):
    has_reqs = bool(state.get("job_requirements"))
    has_jd = bool(state.get("job_description"))
    if not has_reqs and has_jd:
        route = "parse_jd_node"
    else:
        route = "human_interaction_node"
    log_agent_action("Workflow routing (start_router)", details=f"Routing to '{route}' (has_requirements={has_reqs}, has_jd={has_jd})")
    return route

def route_from_human(state: AgentState):
    feedback = state.get("feedback", "")
    if feedback == "new_search":
        route = "parse_jd_node"
    elif feedback == "adjust_requirements": 
        route = "extract_requirements_node"
    elif feedback in ("compare_candidates", "database_query", "general_query"): 
        route = "tool_execution_node"
    else:
        route = "tool_execution_node" # Default fallback
    log_agent_action("Workflow routing (route_from_human)", details=f"Routing to '{route}' based on feedback '{feedback}'")
    return route

def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("parse_jd_node", parse_jd_node)
    builder.add_node("extract_requirements_node", extract_requirements_node)
    builder.add_node("search_resumes_node", search_resumes_node)
    builder.add_node("multi_round_screening_node", multi_round_screening_node)
    builder.add_node("generate_report_node", generate_report_node)
    builder.add_node("human_interaction_node", human_interaction_node)
    builder.add_node("tool_execution_node", tool_execution_node)
    
    builder.add_conditional_edges(START, start_router)
    builder.add_edge("parse_jd_node", "extract_requirements_node")
    builder.add_edge("extract_requirements_node", "search_resumes_node")
    builder.add_edge("search_resumes_node", "multi_round_screening_node")
    builder.add_edge("multi_round_screening_node", "generate_report_node")
    builder.add_edge("generate_report_node", END)
    
    builder.add_conditional_edges(
        "human_interaction_node",
        route_from_human,
        {
            "parse_jd_node": "parse_jd_node",
            "extract_requirements_node": "extract_requirements_node",
            "tool_execution_node": "tool_execution_node"
        }
    )
    builder.add_edge("tool_execution_node", END)
    
    return builder.compile()

if __name__ == "__main__":
    agent_app = build_graph()
    print("Graph compiled successfully (Phase 4).")


