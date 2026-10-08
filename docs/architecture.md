# System Architecture: Agentic Profile Matching

This document provides a detailed architectural blueprint for the Agentic Profile Matching system, based on the project requirements. It serves as a comprehensive reference for the implementation phase.

## 1. High-Level System Overview
The system is an AI-powered conversational agent built using **LangGraph**. It acts as an intelligent recruiter capable of ingesting job descriptions, extracting requirements, matching them against a resume database (using RAG), executing a multi-round screening process, and interacting with users via a **Gradio** chat interface.

---

## 2. Agent State Design (`State`)

The core of the LangGraph agent is its State. The state object will be passed between nodes and mutated at each step. It should be implemented as a `TypedDict` or a `Pydantic` model.

```python
from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    conversation_history: List[Dict[str, str]] # List of messages: {"role": "user"|"assistant", "content": "..."}
    job_description: str                       # Raw job description text
    job_requirements: Dict[str, Any]           # Parsed requirements (must-haves, nice-to-haves)
    candidate_shortlist: List[Dict[str, Any]]  # Current active list of candidates with scores
    candidate_reasoning: Dict[str, str]        # Reasoning for each candidate's ranking/selection
    current_phase: str                         # e.g., "InitialScreen", "DeepAnalysis", "FinalRecommendation"
    feedback: str                              # Human feedback provided for iterative refinement
```

---

## 3. Graph Workflow (Nodes and Edges)

The system operates as a Directed Cyclic Graph (due to the feedback loop), defining the step-by-step workflow of the agent.

### Nodes (Functions/Agents)
1. **`parse_jd_node`**: Receives the raw Job Description (JD) and prepares it for extraction.
2. **`extract_requirements_node`**: Uses the `extract_requirements` tool to populate the `job_requirements` state field.
3. **`search_resumes_node`**: Interacts with the RAG Search tool to query the resume database and retrieve a broad list of candidates (e.g., initial pool of 100).
4. **`multi_round_screening_node`**:
    - *Round 1 (Initial Screen):* Filters the broad pool down to the top 10 candidates.
    - *Round 2 (Deep Analysis):* Performs a thorough analysis of the top 10 against the specific extracted requirements.
    - *Round 3 (Final Decision):* Generates definitive hire/no-hire recommendations for the top candidates.
5. **`generate_report_node`**: Compiles the findings into a detailed match report highlighting strengths, gaps, and improvement suggestions for borderline candidates.
6. **`human_interaction_node`**: Handles the conversational aspect. Processes natural language queries, answers questions (e.g., "Why did John rank higher?"), and accepts requirement adjustments.

### Edges (Routing)
- `START` &rarr; `parse_jd_node`
- `parse_jd_node` &rarr; `extract_requirements_node`
- `extract_requirements_node` &rarr; `search_resumes_node`
- `search_resumes_node` &rarr; `multi_round_screening_node`
- `multi_round_screening_node` &rarr; `generate_report_node`
- `generate_report_node` &rarr; `human_interaction_node`
- **Conditional Edges from `human_interaction_node`:**
  - *Condition 1 (Requirement Adjustment):* If user provides feedback adjusting requirements &rarr; Route back to `extract_requirements_node` or `search_resumes_node`.
  - *Condition 2 (Analysis/Comparison Query):* If user asks a question requiring tools (like `compare_candidates`) &rarr; Route to a Tool Execution node, then back to `human_interaction_node`.
  - *Condition 3 (End):* If user is satisfied / ends session &rarr; `END`.

---

## 4. Tool Specifications

The agent will be equipped with specific tools to perform its tasks. These should be implemented as LangChain `@tool` functions and bound to the agent.

### 4.1. `extract_requirements`
- **Input:** `jd` (string) - The raw job description.
- **Output:** JSON/Dictionary containing `must_have_skills`, `nice_to_have_skills`, `experience_years`, etc.
- **Purpose:** Used early in the graph to parse the JD and structure the search criteria.

### 4.2. `compare_candidates`
- **Input:** `candidate_ids` (List[string]) - IDs or names of candidates to compare.
- **Output:** A head-to-head structured text or Markdown table comparing strengths, weaknesses, and requirement fulfillment side-by-side.
- **Purpose:** Triggered when the user asks to "Compare the top X matches".

### 4.3. `generate_interview_questions`
- **Input:** `candidate_id` (string).
- **Output:** List of tailored screening questions.
- **Purpose:** Addresses specific gaps or verifies strengths identified during the deep analysis phase.

### 4.4. Existing Tools (From Previous Milestones)
- **`rag_search(query: str)`**: Searches the vectorized resume database to find relevant matches.
- **`file_system_tools`**: Tools for reading raw resume files or storing reports if needed.

---

## 5. Frontend Integration (Gradio Chat Interface)

The `human_interaction_node` connects directly to the Gradio frontend to facilitate the interactive features (Part B of the requirements).

**Gradio Flow:**
1. User provides a Job Description in the UI.
2. The LangGraph pipeline begins execution (`START` &rarr; `generate_report_node`).
3. The UI displays the detailed match report and recommendations in the chat interface.
4. User types a natural language query in the chatbox (e.g., *"Find me candidates with React and 3+ years experience"* or *"Why did John rank higher than Jane?"*).
5. Gradio sends this message to the agent's state (`conversation_history` / `feedback`).
6. The graph processes the input, routes to the appropriate node (or executes tools), and streams the response back to the user.

---

## 6. Recommended Project Structure

```text
RAGBasedProfileMatching/
│
├── matching_agent.py          # Core LangGraph implementation (Nodes, Edges, Graph compilation)
├── state.py                   # State TypedDict/Pydantic definition
├── tools.py                   # Implementation of tools (extract, compare, interview_questions)
├── multi_round_screen.py      # Logic for the 3-round filtering process
├── app.py                     # Gradio frontend interface
├── docs/                      
│   ├── ProblemStatement.md    # Source requirements
│   └── architecture.md        # This architecture blueprint
└── jds/                       # Sample Job Descriptions
```
