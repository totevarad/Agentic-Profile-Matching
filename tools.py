import json
from langchain_core.tools import tool
import sys
import os

# Append paths to load tools from previous milestones
sys.path.append(os.path.join(os.path.dirname(__file__), "File_System_Tools"))
sys.path.append(os.path.join(os.path.dirname(__file__), "RAG_Search_Tool"))

try:
    from fs_tools import read_file, list_files, write_file, search_in_file
except ImportError:
    print("Warning: Could not import fs_tools")

@tool
def extract_requirements(jd: str) -> str:
    """
    Parses job descriptions to distinguish between must-have and nice-to-have skills.
    Returns a JSON string representing the requirements.
    """
    # Placeholder mocked output for Phase 1 & 2 evaluation
    return json.dumps({
        "must_have_skills": ["Python", "Machine Learning"],
        "nice_to_have_skills": ["LangChain", "Gradio"],
        "experience_years": 3,
        "role_responsibilities": "Develop agentic workflows."
    })

@tool
def compare_candidates(candidate_ids: list) -> str:
    """
    Performs a head-to-head comparison of candidates given their IDs.
    Returns a markdown table comparing their profiles.
    """
    if not candidate_ids:
        return "No candidates to compare."
    
    # Mocked output for Phase 1 & 2
    return f"| Candidate ID | Strengths | Gaps |\n|---|---|---|\n| {candidate_ids[0]} | Strong Python | Missing Cloud |"

@tool
def generate_interview_questions(candidate_id: str) -> str:
    """
    Creates tailored screening questions for a specific candidate based on identified gaps.
    """
    # Mocked output for Phase 1 & 2
    return f"1. Can you explain your experience with Cloud Deployment, as it seems missing from your profile ({candidate_id})?"

@tool
def rag_search(query: str) -> str:
    """
    Searches the vectorized resume database to find relevant matches.
    Returns a JSON string of candidate IDs and metadata.
    """
    # Mocked RAG search for Pipeline integration in Phase 2
    return json.dumps([
        {"candidate_id": "cand_001", "name": "Alice Smith", "score": 0.95},
        {"candidate_id": "cand_002", "name": "Bob Jones", "score": 0.88},
        {"candidate_id": "cand_003", "name": "Charlie Brown", "score": 0.75}
    ])
