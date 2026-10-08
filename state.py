import operator
from typing import TypedDict, List, Dict, Any, Annotated

class AgentState(TypedDict):
    conversation_history: Annotated[List[Dict[str, str]], operator.add]
    job_description: str
    job_requirements: Dict[str, Any]
    candidate_shortlist: List[Dict[str, Any]]
    candidate_reasoning: Dict[str, str]
    current_phase: str
    feedback: str
