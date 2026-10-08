# Test Scenarios: 5 Conversation Flows

This document outlines five distinct end-to-end conversation flows demonstrating the agent's interactive capabilities. 

---

## Flow 1: Initial JD Ingestion & Report Generation (Happy Path)
**User Action:** User pastes the following job description into the chat interface:
> *"Looking for a Senior Python Developer with Machine Learning experience. 3+ years experience required."*
**Agent Action:**
1. Traverses the main pipeline (`parse_jd` -> `extract_requirements` -> `search_resumes` -> `multi_round_screening` -> `generate_report`).
2. Outputs a detailed Match Report listing the Top candidates (e.g., Alice Smith), their scores, reasoning, and a Hire/No-Hire decision.

---

## Flow 2: Iterative Refinement (Adjusting Requirements)
**User Action:** After reviewing the initial report, the user types:
> *"Actually, we also strictly need someone with React experience."*
**Agent Action:**
1. `human_interaction_node` detects the intent to adjust requirements.
2. Routes backward to `extract_requirements_node`.
3. The state's `job_requirements` is updated to include "React" as a must-have.
4. Pipeline re-runs: Searches resumes again, executes the multi-round screening, and outputs a freshly ranked match report.

---

## Flow 3: Head-to-Head Comparison
**User Action:** The user wants to decide between the top two candidates and types:
> *"Compare the top 2 matches side by side."*
**Agent Action:**
1. `human_interaction_node` detects the comparison intent.
2. Routes to `tool_execution_node`.
3. Invokes the `compare_candidates` tool with the IDs of the top 2 candidates.
4. Outputs a Markdown table comparing their specific strengths and missing gaps based on the requirements.

---

## Flow 4: Explaining Rankings
**User Action:** The user questions the agent's logic:
> *"Why did Alice rank higher than Bob?"*
**Agent Action:**
1. `human_interaction_node` categorizes this as a general reasoning query.
2. Routes to `tool_execution_node`.
3. The LLM accesses the `candidate_reasoning` dictionary from the state.
4. Outputs a transparent explanation (e.g., *"Alice scored 0.95 because she met all must-haves, whereas Bob lacked cloud experience, giving him a score of 0.88."*).

---

## Flow 5: Borderline Candidate Follow-up
**User Action:** The user spots a "No-Hire" borderline candidate and types:
> *"Can you generate interview questions for Charlie to test his missing skills?"*
**Agent Action:**
1. `human_interaction_node` detects the tool execution intent.
2. Routes to `tool_execution_node`.
3. Invokes `generate_interview_questions` for Charlie's ID.
4. Outputs tailored questions addressing Charlie's specific gaps identified during the deep analysis round.
