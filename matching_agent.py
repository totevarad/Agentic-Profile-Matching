import json
from langgraph.graph import StateGraph, START, END
from state import AgentState
from tools import extract_requirements, rag_search, compare_candidates

def parse_jd_node(state: AgentState):
    jd = state.get("job_description", "")
    print(f"[Node: parse_jd_node] Parsing JD (length: {len(jd)})")
    return {"job_description": jd.strip()}

def extract_requirements_node(state: AgentState):
    jd = state.get("job_description", "")
    print("[Node: extract_requirements_node] Extracting requirements...")
    req_json_str = extract_requirements.invoke({"jd": jd})
    req_dict = json.loads(req_json_str)
    
    # If this was a refinement, append the feedback to the JD logic (mocked)
    hist = state.get("conversation_history", [])
    if hist and hist[-1].get("role") == "user":
        user_msg = hist[-1].get("content", "").lower()
        if "react" in user_msg and "React" not in req_dict.get("must_have_skills", []):
            req_dict["must_have_skills"].append("React")
            
    return {"job_requirements": req_dict}

def search_resumes_node(state: AgentState):
    reqs = state.get("job_requirements", {})
    print("[Node: search_resumes_node] Searching resumes based on requirements...")
    query = f"Must have: {reqs.get('must_have_skills')} Nice to have: {reqs.get('nice_to_have_skills')}"
    candidates_json_str = rag_search.invoke({"query": query})
    candidates_list = json.loads(candidates_json_str)
    return {"candidate_shortlist": candidates_list}

def multi_round_screening_node(state: AgentState):
    candidates = state.get("candidate_shortlist", [])
    print("[Node: multi_round_screening_node] Starting multi-round screening...")
    candidates = sorted(candidates, key=lambda x: x.get("score", 0), reverse=True)
    top_candidates = candidates[:10]
    
    reasoning = {}
    for cand in top_candidates:
        score = cand.get("score", 0)
        if score > 0.9: reasoning[cand["candidate_id"]] = "Excellent match across all must-haves."
        elif score > 0.8: reasoning[cand["candidate_id"]] = "Good match but missing some nice-to-haves."
        else: reasoning[cand["candidate_id"]] = "Borderline match."
            
    for cand in top_candidates:
        score = cand.get("score", 0)
        cand["decision"] = "Hire" if score >= 0.85 else "No-Hire"
        
    return {"candidate_shortlist": top_candidates, "candidate_reasoning": reasoning, "current_phase": "ScreeningComplete"}

def generate_report_node(state: AgentState):
    top_candidates = state.get("candidate_shortlist", [])
    reasoning = state.get("candidate_reasoning", {})
    print("[Node: generate_report_node] Generating match report...")
    
    report = "### Candidate Match Report\n\n"
    for cand in top_candidates:
        cid = cand["candidate_id"]
        report += f"**{cand['name']}** ({cand['decision']})\n"
        report += f"- Score: {cand.get('score')}\n"
        report += f"- Reasoning: {reasoning.get(cid, 'No reasoning provided.')}\n\n"
        
    return {"conversation_history": [{"role": "assistant", "content": report}], "feedback": "report_generated"}

def human_interaction_node(state: AgentState):
    print("[Node: human_interaction_node] Processing user input...")
    history = state.get("conversation_history", [])
    if not history: return {"feedback": "none"}
        
    last_msg = history[-1]["content"].lower()
    if "requirement" in last_msg or "adjust" in last_msg or "must-have" in last_msg or "react" in last_msg:
        return {"feedback": "adjust_requirements"}
    elif "compare" in last_msg:
        return {"feedback": "compare_candidates"}
    else:
        return {"feedback": "general_query"}

def tool_execution_node(state: AgentState):
    print("[Node: tool_execution_node] Executing requested tool...")
    feedback = state.get("feedback", "")
    if feedback == "compare_candidates":
        cands = [c["candidate_id"] for c in state.get("candidate_shortlist", [])[:2]]
        res = compare_candidates.invoke({"candidate_ids": cands})
        return {"conversation_history": [{"role": "assistant", "content": res}]}
    return {"conversation_history": [{"role": "assistant", "content": "I can help adjust requirements or compare candidates."}]}

def start_router(state: AgentState):
    if not state.get("job_requirements"):
        return "parse_jd_node"
    return "human_interaction_node"

def route_from_human(state: AgentState):
    feedback = state.get("feedback", "")
    if feedback == "adjust_requirements": return "extract_requirements_node"
    elif feedback == "compare_candidates": return "tool_execution_node"
    return "tool_execution_node" # Default fallback for general queries

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
    
    builder.add_conditional_edges("human_interaction_node", route_from_human)
    builder.add_edge("tool_execution_node", END)
    
    return builder.compile()

if __name__ == "__main__":
    agent_app = build_graph()
    print("Graph compiled successfully (Phase 4).")
