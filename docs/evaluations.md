# Evaluation Criteria: Agentic Profile Matching

This document provides the evaluation checklists for each phase defined in `implementationPlan.md`. Use these to ensure the implementation is correct and meets the requirements before moving to the next phase.

---

## Phase 1 Evaluation: Foundation and State Design
- [ ] **State Structure:** Does `AgentState` correctly include all required fields (`conversation_history`, `job_description`, `job_requirements`, `candidate_shortlist`, `candidate_reasoning`, `current_phase`, `feedback`)?
- [ ] **Tool 1 (`extract_requirements`):** When passed a sample JD, does it accurately return a structured JSON/Dict separating must-haves, nice-to-haves, and experience?
- [ ] **Tool 2 (`compare_candidates`):** Can it take two candidate profiles and generate a clear, side-by-side comparison (e.g., Markdown table)?
- [ ] **Tool 3 (`generate_interview_questions`):** Does it generate contextually relevant screening questions based on a specific candidate's gaps?
- [ ] **Legacy Tools:** Are the RAG search and File System tools successfully imported and callable?

---

## Phase 2 Evaluation: Core LangGraph Pipeline
- [ ] **Graph Compilation:** Does the basic LangGraph compile without errors?
- [ ] **JD Parsing:** Is the raw text of the Job Description correctly ingested by `parse_jd_node`?
- [ ] **State Mutation (Requirements):** After `extract_requirements_node` runs, is `state["job_requirements"]` populated correctly?
- [ ] **State Mutation (Resumes):** After `search_resumes_node` runs, does `state["candidate_shortlist"]` contain a list of retrieved candidates from the RAG tool?
- [ ] **Pipeline Execution:** Can the graph successfully execute from `START` to the end of the resume search phase without hanging?

---

## Phase 3 Evaluation: Advanced Screening & Reporting
- [ ] **Screening Round 1:** Does the agent successfully filter the broad list down to a precise top 10?
- [ ] **Screening Round 2 (Deep Analysis):** Are the top 10 candidates deeply analyzed against the extracted requirements, and is this stored in `candidate_reasoning`?
- [ ] **Screening Round 3:** Does the system produce clear "hire" or "no-hire" recommendations for the top candidates?
- [ ] **Report Output:** Does `generate_report_node` output a structured report that explicitly includes:
  - Strengths and gaps for each candidate?
  - Improvement suggestions for borderline candidates?

---

## Phase 4 Evaluation: Interactive Interface & Feedback Loop
- [ ] **Gradio UI:** Is the Gradio chat interface responsive and capable of sending messages to the agent?
- [ ] **Natural Language Querying:** Can the agent understand and respond to queries like *"Find me candidates with React and 3+ years experience"*?
- [ ] **Tool Triggering via Chat:** If a user asks *"Compare the top 3 matches"*, does the agent correctly route to and execute `compare_candidates`?
- [ ] **Iterative Refinement (Crucial):** 
  - If a user changes a requirement (e.g., *"Actually, Python is a must-have now"*), does the graph correctly route backward?
  - Are candidates re-ranked?
  - Does the agent clearly explain the changes in the new rankings?

---

## Phase 5 Evaluation: Finalization & Deliverables
- [ ] **Conversation Flows:** Are 5 distinct conversational scenarios documented and successfully executing?
- [ ] **Diagram:** Is a clear State Machine diagram (visual representation of the LangGraph) included in the repository?
- [ ] **Code Quality:** Is the code clean, modular (`tools.py`, `state.py`, `app.py`), and well-commented?
- [ ] **Demo Video:** Does the 5-6 minute video clearly demonstrate the agent's reasoning process, the multi-round screening, and the interactive requirement adjustments?
