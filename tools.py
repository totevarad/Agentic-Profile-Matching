import json
import os
import sys
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

from agent_logger import (
    logger,
    log_agent_action,
    log_agent_reasoning,
    timed_llm_invoke,
)

load_dotenv()

# Append paths to load tools from previous milestones
sys.path.append(os.path.join(os.path.dirname(__file__), "File_System_Tools"))
sys.path.append(os.path.join(os.path.dirname(__file__), "RAG_Search_Tool"))

# Initialize LLM
try:
    llm = ChatOpenAI(
        model="apodex/apodex-1.1-mini:free", 
        temperature=0.2,
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )
except Exception as e:
    logger.warning(f"Could not initialize OpenRouter: {e}")
    llm = None

# Initialize Chroma and Embeddings
try:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
except Exception as e:
    logger.warning(f"Could not initialize Chroma DB: {e}")
    vectorstore = None

@tool
def extract_requirements(jd: str) -> str:
    """
    Parses job descriptions to distinguish between must-have and nice-to-have skills.
    Returns a JSON string representing the requirements.
    """
    log_agent_action("Tool invoked: extract_requirements", details=f"JD length: {len(jd)} characters")
    if not llm:
        log_agent_action("LLM not initialized in extract_requirements tool")
        return json.dumps({
            "must_have_skills": ["Error: LLM not initialized"],
            "nice_to_have_skills": [],
            "experience_years": 0,
            "role_responsibilities": "N/A"
        })
        
    prompt = f"""
    You are an expert HR recruiter. Analyze the following Job Description and extract the key requirements.
    Return ONLY a valid JSON object with the following keys:
    - must_have_skills: list of strings
    - nice_to_have_skills: list of strings
    - experience_years: integer (use 0 if not specified)
    - role_responsibilities: string

    Job Description:
    {jd}
    """
    _, duration, content_str = timed_llm_invoke(
        llm,
        prompt,
        task_name="Tool: extract_requirements",
        extract_reasoning=False
    )
    content = content_str.replace("```json", "").replace("```", "").strip()
    log_agent_reasoning("Tool: extract_requirements parsed JSON", content)
    return content

@tool
def compare_candidates(candidate_ids: list) -> str:
    """
    Performs a head-to-head comparison of candidates given their IDs.
    Returns a markdown table comparing their profiles.
    """
    log_agent_action("Tool invoked: compare_candidates", details=f"Candidate IDs: {candidate_ids}")
    if not candidate_ids or not llm:
        msg = "No candidates to compare or LLM not initialized."
        log_agent_action("compare_candidates aborted", details=msg)
        return msg
    
    prompt = f"""
    Write a professional markdown comparison for candidates with these IDs: {candidate_ids}. 
    Since this is a simulated tool, provide a realistic hypothetical comparison of their strengths and gaps in a markdown table format.
    """
    _, duration, content_str = timed_llm_invoke(
        llm,
        prompt,
        task_name=f"Tool: compare_candidates ({candidate_ids})",
        extract_reasoning=True
    )
    return content_str

@tool
def generate_interview_questions(candidate_id: str) -> str:
    """
    Creates tailored screening questions for a specific candidate based on identified gaps.
    """
    log_agent_action("Tool invoked: generate_interview_questions", details=f"Candidate ID: {candidate_id}")
    if not llm:
        msg = "LLM not initialized."
        log_agent_action("generate_interview_questions aborted", details=msg)
        return msg
        
    prompt = f"Generate 3 tailored technical screening interview questions for a candidate with ID: {candidate_id} to probe potential gaps."
    _, duration, content_str = timed_llm_invoke(
        llm,
        prompt,
        task_name=f"Tool: generate_interview_questions ({candidate_id})",
        extract_reasoning=True
    )
    return content_str

@tool
def rag_search(query: str) -> str:
    """
    Searches the vectorized resume database to find relevant matches.
    Returns a JSON string of candidate IDs and metadata.
    """
    log_agent_action("Tool invoked: rag_search", details=f"Query: '{query}'")
    if not vectorstore:
        log_agent_action("rag_search failed: Chroma DB not initialized")
        return json.dumps([{"candidate_id": "error", "name": "Chroma DB not found", "score": 0}])
        
    results_with_score = vectorstore.similarity_search_with_score(query, k=5)
    
    candidates = []
    seen = set()
    
    for doc, distance in results_with_score:
        meta = doc.metadata
        name = meta.get("name", "Unknown").replace(".pdf", "").replace(".docx", "")
        cid = "cand_" + name.replace(" ", "_").lower()
        
        if cid not in seen:
            # Convert distance to a mock score (lower distance = higher score)
            score = max(0.0, 1.0 - (distance / 2.0)) 
            
            candidates.append({
                "candidate_id": cid,
                "name": name,
                "score": round(score, 2),
                "skills": meta.get("skills_str", ""),
                "experience": meta.get("years_of_experience", 0)
            })
            seen.add(cid)
            
    candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)
    log_agent_action("rag_search completed", details=f"Found {len(candidates)} candidates")
    return json.dumps(candidates)

