
# Agentic Profile Matching

Agentic Profile Matching is an intelligent, agent-based application built using LangGraph, LangChain, and Gradio. It assists recruiters and hiring managers in automating the candidate screening process by matching a given Job Description (JD) against candidate profiles.

## What is the use of this application?
The application streamlines the hiring process by automatically parsing Job Descriptions to extract core requirements. It then searches for suitable candidates (using a mocked Retrieval-Augmented Generation search), evaluates them based on the criteria, and generates a comprehensive match report. Furthermore, it supports human-in-the-loop interactions, allowing users to dynamically adjust requirements or compare top candidates through a chat interface.

## Features
- **Automated JD Parsing & Extraction:** Automatically extracts "must-have" and "nice-to-have" skills, along with experience requirements, from any pasted Job Description.
- **Candidate Retrieval (RAG Search):** Uses a RAG-based search to find relevant resumes based on the extracted job requirements.
- **Multi-Round Candidate Screening:** Scores candidates based on their match to the requirements and makes preliminary "Hire" or "No-Hire" recommendations.
- **Match Report Generation:** Provides a detailed markdown report for the top candidates, including scores and the reasoning behind their evaluation.
- **Interactive Chat Interface:** Users can chat with the agent to:
  - Adjust requirements (e.g., "Add React as a must-have skill").
  - Request head-to-head comparisons of the top candidates.
- **Agentic Workflow:** Utilizes a stateful LangGraph workflow to navigate between parsing, searching, screening, reporting, and tool execution phases.

## How to start the application
1. **Install Dependencies:**
   Ensure you have Python installed. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```
2. **Process Resumes and Setup Database:**
   Place your candidate resumes (PDF or DOCX format) in the `resumes` folder in the root directory (create the folder if it doesn't exist). To trigger the RAG pipeline to do the embedding and store it in Chroma DB, run:
   ```bash
   python RAG_Search_Tool/resume_rag.py
   ```
3. **Run the Application:**
   Execute the main application script:
   ```bash
   python app.py
   ```
4. **Access the UI:**
   The terminal will output a local URL (typically `http://127.0.0.1:7860`). Open this link in your web browser to access the Gradio chat interface.

## How to use the application
1. **Initial Input:** Once the Gradio interface is open, paste your full Job Description into the chat box and hit submit.
2. **Review the Report:** The agent will process the JD, run the screening pipeline, and reply with a "Candidate Match Report" detailing the top matches and their scores.
3. **Interact and Refine:** You can continue the conversation by typing queries such as:
   - *"Actually, make React a must-have requirement."*
   - *"Compare the top two candidates."*
   The agent will dynamically adjust its state and execute the relevant tools to respond to your request.

## File Structure and Meaning
- **`app.py`**: The main entry point of the application. It initializes the Gradio chat interface and maintains the global session state to persist the agent's memory across chat messages.
- **`matching_agent.py`**: Contains the core LangGraph state machine. It defines all the graph nodes (e.g., `parse_jd_node`, `extract_requirements_node`, `search_resumes_node`, `multi_round_screening_node`, etc.) and the conditional routing logic that drives the agent's decision-making.
- **`tools.py`**: Defines the LangChain `@tool` functions used by the agent. This includes functions for extracting requirements, comparing candidates, generating interview questions, and performing the RAG search.
- **`state.py`**: Defines the `AgentState` TypedDict. This file dictates the structure of the state object passed between nodes in the LangGraph, tracking history, requirements, and candidate data.
- **`requirements.txt`**: A list of Python dependencies (like `langchain`, `langgraph`, `gradio`, etc.) needed to run the project.
- **`File_System_Tools/` & `RAG_Search_Tool/`**: Directories containing supplementary modules and tool implementations from previous development phases, dealing with file operations and document retrieval.
- **`agent_logger.py`**: Centralized structured logging module tracking user prompts, agent actions, LLM latency/response times, and qualitative reasoning into `log/app.log`.
- **`log/app.log`**: Output audit log file recording all user interactions, agent state decisions, LLM response timing, and screening reasoning.
- **`docs/`**: Project documentation, including:
  - [`architecture.md`](docs/architecture.md): High-level system architecture and agent state machine diagram.
  - [`stateMachine.md`](docs/stateMachine.md): Dedicated state machine specification, Mermaid workflow diagrams, and state transitions.

## What is text used for in this app?
Text processing is the core of this application. Unstructured text from Job Descriptions is parsed into structured JSON criteria. The simulated resume texts are then evaluated against these criteria using language models (or mocked tool logic). Finally, text generation is used to produce human-readable match reports, reasoning summaries, and conversational responses in the chat interface.
