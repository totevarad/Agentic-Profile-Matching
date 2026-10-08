import gradio as gr
from matching_agent import build_graph

agent_app = build_graph()

# Global state to persist the agent's memory during the session
session_state = {
    "job_description": "",
    "conversation_history": [],
    "job_requirements": {},
    "candidate_shortlist": [],
    "candidate_reasoning": {},
    "current_phase": "InitialScreen",
    "feedback": ""
}

def chat_interface(message, history):
    global session_state
    
    # First message is treated as the Job Description upload
    if not session_state.get("job_requirements"):
        session_state["job_description"] = message
        # Execute initial pipeline
        session_state = agent_app.invoke(session_state)
        # Return the generated report
        return session_state["conversation_history"][-1]["content"]
        
    # Subsequent messages are interactive queries
    session_state["conversation_history"].append({"role": "user", "content": message})
    session_state = agent_app.invoke(session_state)
    
    # Return the latest response from the agent
    return session_state["conversation_history"][-1]["content"]

demo = gr.ChatInterface(
    fn=chat_interface,
    title="Agentic Profile Matching",
    description="Paste a Job Description to start, then ask questions or refine requirements!"
)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
