# State Machine & Workflow Specification: Agentic Profile Matching

This document provides a comprehensive state machine specification and visual diagrams for the LangGraph-based conversational screening agent.

---

## 1. Visual Flowchart & State Machine

```mermaid
flowchart TD
    %% Node styling
    classDef terminal fill:#0f172a,stroke:#475569,stroke-width:2px,color:#f8fafc;
    classDef router fill:#f59e0b,stroke:#b45309,stroke-width:2px,color:#1e293b,font-weight:bold;
    classDef pipe fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#ffffff;
    classDef interact fill:#0f766e,stroke:#115e59,stroke-width:2px,color:#ffffff;
    classDef tool fill:#6d28d9,stroke:#5b21b6,stroke-width:2px,color:#ffffff;

    START((START)):::terminal --> startRouter{"start_router<br/>(Check State)"}:::router

    %% Pipeline Subgraph
    subgraph Pipeline ["Batch Processing & Candidate Screening Pipeline"]
        direction TD
        parse["<b>parse_jd_node</b><br/>Cleans & trims JD text"]:::pipe
        extract["<b>extract_requirements_node</b><br/>Extracts structured skills via LLM"]:::pipe
        search["<b>search_resumes_node</b><br/>Executes ChromaDB RAG search"]:::pipe
        screen["<b>multi_round_screening_node</b><br/>Scores top 5, generates reasoning & Hire/No-Hire"]:::pipe
        report["<b>generate_report_node</b><br/>Builds markdown Candidate Match Report"]:::pipe

        parse --> extract
        extract --> search
        search --> screen
        screen --> report
    end

    %% Conversational Loop Subgraph
    subgraph HumanInteraction ["Conversational Interaction & Feedback Loop"]
        direction TD
        human["<b>human_interaction_node</b><br/>Classifies user intent via LLM"]:::interact
        routeHuman{"route_from_human<br/>(Branch on Intent)"}:::router
        toolExec["<b>tool_execution_node</b><br/>Executes candidate comparison or contextual Q&A"]:::tool
        
        human --> routeHuman
    end

    %% Start Routing Decisions
    startRouter -- "New JD uploaded<br/>(requirements empty)" --> parse
    startRouter -- "Chat turn in active session" --> human

    %% Human Routing Branches
    routeHuman -- "adjust_requirements<br/>(Loop back with updated criteria)" --> extract
    routeHuman -- "compare_candidates<br/>(Head-to-head evaluation)" --> toolExec
    routeHuman -- "general_query<br/>(Contextual Q&A on candidates)" --> toolExec

    %% Terminal Endpoints
    report --> END((END)):::terminal
    toolExec --> END((END)):::terminal
```

---

## 2. State Lifecycle Diagram

The agent operates across distinct lifecycle states stored in `AgentState`:

```mermaid
stateDiagram-v2
    [*] --> Idle: Application Start

    state "JD Ingestion & Extraction" as Ingestion {
        [*] --> JD_Parsing
        JD_Parsing --> Requirements_Extraction: extract_requirements tool
    }

    state "Resume Retrieval & Analysis" as Matching {
        [*] --> RAG_Retrieval: rag_search tool
        RAG_Retrieval --> Multi_Round_Screening: Top-k ranking & reasoning
        Multi_Round_Screening --> Report_Ready: generate_report_node
    }

    state "Human Interaction Turn" as InteractiveTurn {
        [*] --> Intent_Classification: human_interaction_node
        Intent_Classification --> Tool_Dispatch: compare_candidates / general_query
        Tool_Dispatch --> Response_Generated: tool_execution_node
    }

    Idle --> Ingestion: User submits Job Description
    Ingestion --> Matching: Criteria extracted
    Matching --> InteractiveTurn: Match report displayed in Gradio
    
    InteractiveTurn --> Ingestion: User adjusts requirements (Feedback Loop)
    InteractiveTurn --> InteractiveTurn: User asks comparison or follow-up question
    InteractiveTurn --> [*]: User closes session
```

---

## 3. Node Specifications & State Mutations

| Node | Input Fields Consumed | State Fields Mutated / Returned | Description & Tools Used |
|---|---|---|---|
| **`parse_jd_node`** | `job_description` | `job_description` | Strips leading/trailing whitespaces and validates length. |
| **`extract_requirements_node`** | `job_description`, `conversation_history` | `job_requirements`, `job_description` | Calls `extract_requirements` tool. If triggered from user feedback, appends feedback to the JD before extraction. |
| **`search_resumes_node`** | `job_requirements` | `candidate_shortlist` | Invokes `rag_search` querying vector database for matching profiles. |
| **`multi_round_screening_node`** | `candidate_shortlist`, `job_requirements` | `candidate_shortlist`, `candidate_reasoning`, `current_phase` | Sorts by score, selects top 5, invokes LLM to generate individualized match reasoning, and assigns "Hire" (score &ge; 0.5) / "No-Hire". |
| **`generate_report_node`** | `candidate_shortlist`, `candidate_reasoning` | `conversation_history`, `feedback` | Generates a structured markdown "Candidate Match Report" and pushes it to `conversation_history`. |
| **`human_interaction_node`** | `conversation_history` | `feedback` | LLM classifies user message intent into `adjust_requirements`, `compare_candidates`, or `general_query`. |
| **`tool_execution_node`** | `candidate_shortlist`, `conversation_history`, `feedback` | `conversation_history` | Invokes `compare_candidates` tool if requested, or runs general Q&A with candidate context. |

---

## 4. Conditional Edge Details

1. **`start_router(state: AgentState)`**:
   - Condition: `not state.get("job_requirements") and state.get("job_description")` &rarr; Routes to `parse_jd_node`.
   - Otherwise &rarr; Routes to `human_interaction_node`.

2. **`route_from_human(state: AgentState)`**:
   - `feedback == "adjust_requirements"` &rarr; Routes to `extract_requirements_node` (completing the iterative refinement loop).
   - `feedback == "compare_candidates"` &rarr; Routes to `tool_execution_node`.
   - Default / `feedback == "general_query"` &rarr; Routes to `tool_execution_node`.

