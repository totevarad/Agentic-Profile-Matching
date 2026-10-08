# State Machine Diagram: Agentic Profile Matching

This diagram outlines the LangGraph execution flow for the conversational screening agent.

```mermaid
stateDiagram-v2
    [*] --> StartRouter
    
    %% Main Pipeline Execution
    StartRouter --> parse_jd_node : Uploads Job Description
    parse_jd_node --> extract_requirements_node
    extract_requirements_node --> search_resumes_node
    search_resumes_node --> multi_round_screening_node
    multi_round_screening_node --> generate_report_node
    generate_report_node --> [*]
    
    %% Interactive Feedback Loop
    StartRouter --> human_interaction_node : Sends Chat Message
    human_interaction_node --> RouteFromHuman
    
    RouteFromHuman --> extract_requirements_node : Intent: Adjust Requirements
    RouteFromHuman --> tool_execution_node : Intent: Execute Tool / Compare
    
    %% Tool execution ends graph step (awaiting next human input)
    tool_execution_node --> [*]
```

### Node Descriptions:
- **`parse_jd_node`**: Cleans and prepares the raw text.
- **`extract_requirements_node`**: Leverages the LLM tool to generate a structured JSON of must-haves and nice-to-haves.
- **`search_resumes_node`**: Triggers the RAG pipeline to pull an initial pool of candidates matching the requirements.
- **`multi_round_screening_node`**: Executes the 3-round filtering process (Top 10 -> Deep Analysis -> Final Decision).
- **`generate_report_node`**: Creates the structured markdown match report.
- **`human_interaction_node`**: Evaluates user queries to determine intent (feedback loop).
- **`tool_execution_node`**: Executes requested functions like `compare_candidates` or `generate_interview_questions`.
