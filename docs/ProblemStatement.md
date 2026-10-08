# Agentic Profile Matching

## Assignment Brief
This project involves building an **Agentic Profile Matching** system. The objective is to create an intelligent agent capable of parsing job descriptions, extracting requirements, searching and ranking candidate resumes, and providing a conversational interface for interactive candidate screening.

---

## Assignment Requirements

### Part A: Agent Architecture (40%)
The core of the system is the `matching_agent.py` script, built using **LangGraph**.

#### 1. Agent State Design
The agent must maintain a structured state to track context throughout the matching process:
- **Conversation History:** Track user interactions and queries.
- **Job Requirements Understanding:** Maintain an active understanding of the target role.
- **Candidate Shortlist & Reasoning:** Store selected candidates and the rationale behind their selection.

#### 2. Agent Workflow (Graph Structure)
The agent should follow this structured graph execution flow:
`START` → `Parse JD` → `Extract Requirements` → `Search Resumes` → `Rank Candidates` → `Generate Report` → `Human Feedback Loop` → `END`

#### 3. Tools Available to the Agent
The agent should have access to the following toolset:
- **File System Tools:** Developed in Milestone 1.
- **RAG Search Tool:** Developed in Milestone 2.
- **Additional Tools:**
  - `extract_requirements(jd: str)`: Parses job descriptions to distinguish between "must-have" and "nice-to-have" skills.
  - `compare_candidates(candidate_ids: list)`: Performs a head-to-head comparison of candidates.
  - `generate_interview_questions(candidate_id: str)`: Creates tailored screening questions for a specific candidate.

---

### Part B: Interactive Features (30%)
The system must provide an interactive, conversational interface.

#### 1. Conversational Interface
The agent should accept and process natural language queries, such as:
- *"Find me candidates with React and 3+ years experience"*
- *"Compare the top 3 matches side by side"*
- *"Why did John rank higher than Jane?"*

#### 2. Iterative Refinement
Users must be able to adjust job requirements mid-conversation. The agent should:
- Re-rank candidates based on the new criteria.
- Clearly explain the changes in the resulting rankings.

---

### Part C: Advanced Capabilities (30%)
The system should demonstrate advanced screening and reasoning capabilities.

#### 1. Multi-Round Screening
Implement a phased approach to candidate filtering:
- **Initial Screen:** Select the top 10 candidates from a pool of 100 resumes.
- **Second Round:** Perform a deep analysis of the top 10 candidates.
- **Final Round:** Generate a definitive "hire" or "no-hire" recommendation.

#### 2. Explainability
The agent must provide transparent reasoning for its decisions:
- Generate detailed match reports.
- Highlight the specific strengths and gaps for each candidate.
- Provide improvement suggestions for borderline candidates.

---

## Submission Guidelines
The final submission must include the following components:
1. **Agent Implementation:** The complete LangGraph-based agent code.
2. **State Machine Diagram:** A visual representation of the agent's graph workflow.
3. **Chat Interface:** A functional UI built using **Gradio**.
4. **Test Scenarios:** Documentation of 5 or more distinct conversation flows demonstrating the agent's capabilities.
5. **Demo Video:** A 5-6 minute video showcasing the agent's reasoning and interactive features.
