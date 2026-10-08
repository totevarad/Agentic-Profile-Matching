# Implementation Plan: Agentic Profile Matching

This document outlines the phase-by-phase implementation plan for building the Agentic Profile Matching system based on the defined architecture and problem statement.

## Phase 1: Foundation and State Design
**Objective:** Set up the project structure, define the agent's memory (state), and implement the core utility tools.
1. **Repository Setup:** Create the fundamental files (`matching_agent.py`, `tools.py`, `state.py`, `app.py`).
2. **State Definition:** Implement the `AgentState` (TypedDict) in `state.py` containing `conversation_history`, `job_description`, `job_requirements`, `candidate_shortlist`, `candidate_reasoning`, `current_phase`, and `feedback`.
3. **Tool Implementation:**
    - Develop `extract_requirements(jd: str)`.
    - Develop `compare_candidates(candidate_ids: list)`.
    - Develop `generate_interview_questions(candidate_id: str)`.
4. **Tool Integration:** Integrate previous milestone tools (RAG search tool, File system tools).

## Phase 2: Core LangGraph Pipeline (Part A)
**Objective:** Build the foundational, non-interactive linear workflow of the agent.
1. **Node Creation:**
    - Implement `parse_jd_node`.
    - Implement `extract_requirements_node`.
    - Implement `search_resumes_node`.
2. **Graph Construction:** Wire these nodes together using LangGraph.
    - `START` &rarr; `parse_jd_node` &rarr; `extract_requirements_node` &rarr; `search_resumes_node`.
3. **Initial Testing:** Ensure that given a raw JD, the agent can successfully extract requirements and retrieve an initial pool of relevant resumes from the RAG tool.

## Phase 3: Advanced Screening & Reporting (Part C)
**Objective:** Implement the multi-stage filtering logic and generate comprehensive match reports.
1. **Multi-Round Screening Node:**
    - *Round 1:* Logic to filter the initial pool (e.g., 100) down to the top 10.
    - *Round 2:* Logic for deep analysis of the top 10 against specific `job_requirements`.
    - *Round 3:* Logic to generate a final hire/no-hire recommendation.
2. **Report Generation Node:** Implement `generate_report_node` to output structured match reports highlighting strengths, gaps, and improvement suggestions for borderline candidates.
3. **Graph Update:** Add these nodes to the LangGraph pipeline (`search_resumes_node` &rarr; `multi_round_screening_node` &rarr; `generate_report_node`).

## Phase 4: Interactive Interface & Feedback Loop (Part B)
**Objective:** Enable dynamic conversations, tool calling based on user queries, and iterative refinement.
1. **Human Interaction Node:** Implement `human_interaction_node` to handle user input and maintain `conversation_history`.
2. **Conditional Routing:** Implement conditional edges from the human interaction node:
    - Route to `extract_requirements_node` or `search_resumes_node` if the user adjusts requirements.
    - Route to specific tools (like `compare_candidates`) if the user asks a question requiring analysis.
    - Route to `END` if the session is complete.
3. **Gradio Frontend:** Build the Chat Interface in `app.py` and connect it to the LangGraph `human_interaction_node`.

## Phase 5: Finalization & Deliverables
**Objective:** Thoroughly test the system, finalize the UI, and prepare submission materials.
1. **End-to-End Testing:** Run and document 5+ distinct conversation flows (e.g., standard flow, refinement flow, comparison flow).
2. **Diagram Generation:** Create the visual State Machine diagram representing the graph structure.
3. **Demo Preparation:** Record the 5-6 minute demo video showcasing the reasoning and interactive features.
