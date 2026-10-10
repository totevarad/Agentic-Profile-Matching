import gradio as gr
from matching_agent import build_graph
from agent_logger import (
    logger,
    log_user_prompt,
    log_agent_action,
)

# Initialize compiled LangGraph agent
agent_app = build_graph()

def get_initial_session_state():
    """Returns a fresh, isolated state dictionary for a chat session."""
    return {
        "job_description": "",
        "conversation_history": [],
        "job_requirements": {},
        "candidate_shortlist": [],
        "candidate_reasoning": {},
        "current_phase": "InitialScreen",
        "feedback": ""
    }

INITIAL_GREETING = (
    "### 👋 Welcome to Agentic Profile Matching!\n\n"
    "I am an intelligent recruitment agent connected to the candidate resume database. Here is what you can do:\n\n"
    "- 📋 **Screen a Job Description:** Paste a full JD to parse must-haves, search resumes, and screen top candidates.\n"
    "- 🔍 **New Candidate Search:** Ask to find specific skill sets (e.g. *\"Find me backend developers with 4+ years of experience\"*).\n"
    "- ❓ **Database Queries:** Ask exploratory questions across all candidates (e.g. *\"Is there any candidate who has less than 3 years of experience and is a UI/UX or frontend developer?\"*).\n"
    "- ⚖️ **Candidate Comparisons:** Ask for head-to-head analysis (e.g. *\"Why does Julia Zhang have a higher score than Xavier?\"*).\n\n"
    "💡 *To start a fresh conversation at any time, click the **➕ New Chat** button on the left.*"
)

# Global fallback state for standalone function invocations (e.g. test scripts)
_global_fallback_state = get_initial_session_state()

def chat_interface(message: str, history=None, current_state=None):
    """
    Core agent pipeline runner.
    Accepts message, history, and session state.
    """
    global _global_fallback_state
    if current_state is None:
        state_to_use = _global_fallback_state
    else:
        state_to_use = current_state
        
    log_user_prompt(message, context="Chat Interface")
    
    # Append user prompt to state conversation history
    state_to_use["conversation_history"].append({"role": "user", "content": message})
    
    # If no JD is currently stored, assign this prompt as the active JD
    if not state_to_use.get("job_requirements") and not state_to_use.get("job_description"):
        state_to_use["job_description"] = message
        log_agent_action("Assigned prompt as new Job Description", details=f"Length: {len(message)} chars")
        
    # Execute LangGraph pipeline
    log_agent_action("Invoking LangGraph pipeline", details={"current_phase": state_to_use.get("current_phase")})
    state_to_use = agent_app.invoke(state_to_use)
    log_agent_action("LangGraph pipeline finished", details={"current_phase": state_to_use.get("current_phase")})
    
    # Fetch assistant response
    response = state_to_use["conversation_history"][-1]["content"]
    log_agent_action("Delivered assistant response to user", details=f"Length: {len(response)} chars")
    
    if current_state is None:
        _global_fallback_state = state_to_use
        return response
    return response, state_to_use

def get_status_markdown(state: dict) -> str:
    """Formats live session info for the sidebar."""
    jd = state.get("job_description", "")
    preview = (jd[:45] + "...") if len(jd) > 45 else (jd if jd else "None (Ready for JD)")
    cands_count = len(state.get("candidate_shortlist", []))
    phase = state.get("current_phase", "InitialScreen")
    return (
        f"**Active Search / JD:**\n> *{preview}*\n\n"
        f"**Shortlisted Pool:** `{cands_count} candidates`\n\n"
        f"**Current Phase:** `{phase}`"
    )

def handle_user_submit(user_message: str, chat_history: list, current_state: dict):
    """Handles user sending a message via Enter or Send button."""
    if not user_message or not user_message.strip():
        return "", chat_history, current_state, get_status_markdown(current_state)
        
    text = user_message.strip()
    history = chat_history or []
    history.append({"role": "user", "content": text})
    
    # Process turn
    reply, updated_state = chat_interface(text, history, current_state)
    history.append({"role": "assistant", "content": reply})
    
    status_md = get_status_markdown(updated_state)
    return "", history, updated_state, status_md

def handle_new_chat():
    """Resets the chat interface and the agent's internal state completely."""
    fresh_state = get_initial_session_state()
    initial_chat = [{"role": "assistant", "content": INITIAL_GREETING}]
    status_md = get_status_markdown(fresh_state)
    log_agent_action("New Chat requested. Reset session state to empty defaults.")
    return initial_chat, fresh_state, status_md, ""

# Custom CSS for modern design and clean styling
custom_css = """
#main-container { max-width: 1200px; margin: auto; padding: 10px; }
#new-chat-btn { background: #2563eb !important; color: white !important; font-weight: 600; border-radius: 8px; }
#new-chat-btn:hover { background: #1d4ed8 !important; }
.example-btn { text-align: left !important; font-size: 0.88rem !important; border-radius: 6px !important; }
#status-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; }
"""

with gr.Blocks(title="Agentic Profile Matching") as demo:
    # Per-session state storage
    session_state_var = gr.State(value=get_initial_session_state())
    
    with gr.Row(elem_id="main-container"):
        # Left Sidebar (Controls & Actions)
        with gr.Column(scale=1, min_width=280):
            gr.Markdown("### 💼 Recruiter Controls")
            new_chat_btn = gr.Button("➕ New Chat", elem_id="new-chat-btn", variant="primary", size="lg")
            
            gr.Markdown("---")
            gr.Markdown("#### 💡 Quick Search Prompts")
            ex_ml = gr.Button("🤖 ML & LLMs (3+ yrs exp)", elem_classes="example-btn")
            ex_backend = gr.Button("💻 Senior Backend (FastAPI, Docker)", elem_classes="example-btn")
            ex_frontend = gr.Button("🎨 Frontend / UI/UX (< 3 yrs exp)", elem_classes="example-btn")
            ex_compare = gr.Button("⚖️ Compare Julia Zhang vs Xavier", elem_classes="example-btn")
            
            gr.Markdown("---")
            gr.Markdown("#### 📊 Session Status")
            status_display = gr.Markdown(value=get_status_markdown(get_initial_session_state()), elem_id="status-card")
            
        # Right Chat Area
        with gr.Column(scale=3):
            gr.Markdown(
                "## 🎯 Agentic Profile Matching\n"
                "*Autonomous candidate screening, RAG vector retrieval, and qualitative LLM evaluation.*"
            )
            
            chatbot = gr.Chatbot(
                value=[{"role": "assistant", "content": INITIAL_GREETING}],
                height=560,
                layout="bubble",
                render_markdown=True,
                buttons=["copy"]
            )
            
            with gr.Row():
                msg_input = gr.Textbox(
                    placeholder="Paste a Job Description, or ask: 'Find me backend engineers...', 'Why does Candidate A score higher?', etc.",
                    lines=2,
                    max_lines=6,
                    scale=5,
                    show_label=False,
                    autofocus=True
                )
                send_btn = gr.Button("Send 🚀", variant="primary", scale=1)
    
    # Event Handlers
    # 1. Send button click
    send_btn.click(
        fn=handle_user_submit,
        inputs=[msg_input, chatbot, session_state_var],
        outputs=[msg_input, chatbot, session_state_var, status_display]
    )
    
    # 2. Enter key submit
    msg_input.submit(
        fn=handle_user_submit,
        inputs=[msg_input, chatbot, session_state_var],
        outputs=[msg_input, chatbot, session_state_var, status_display]
    )
    
    # 3. New Chat button click
    new_chat_btn.click(
        fn=handle_new_chat,
        inputs=[],
        outputs=[chatbot, session_state_var, status_display, msg_input]
    )
    
    # 4. Quick Prompts
    ex_ml.click(
        fn=lambda: "Hello, find me candidates related to machine learning and AI who have specific skill sets in transformers and LLMs, with 3+ years of experience.",
        outputs=[msg_input]
    )
    ex_backend.click(
        fn=lambda: "Find me candidates with backend development experience, their strongest skill set in backend, and the number of years of relevant experience.",
        outputs=[msg_input]
    )
    ex_frontend.click(
        fn=lambda: "Is there any candidate who has less than 3 years of experience and is a UI/UX or frontend developer?",
        outputs=[msg_input]
    )
    ex_compare.click(
        fn=lambda: "Why does Julia Zhang have a higher score than Xavier?",
        outputs=[msg_input]
    )

if __name__ == "__main__":
    log_agent_action("Starting Gradio application server on 127.0.0.1:7860")
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        css=custom_css,
        theme=gr.themes.Soft()
    )
