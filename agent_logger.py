import os
import sys
import time
import logging
from typing import Any, Optional, Tuple, Dict

# Resolve project root and log directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(PROJECT_ROOT, "log")
LOG_FILE = os.path.join(LOG_DIR, "app.log")

def setup_logger(
    name: str = "AgentLogger",
    log_file: str = LOG_FILE,
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configures and returns a centralized logger that outputs formatted logs
    to both `log/app.log` (UTF-8 encoded) and stdout.
    """
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logger_instance = logging.getLogger(name)
    logger_instance.setLevel(level)

    abs_log_path = os.path.abspath(log_file)
    
    # Avoid duplicate FileHandlers
    has_file_handler = any(
        isinstance(h, logging.FileHandler) and getattr(h, "baseFilename", "") == abs_log_path
        for h in logger_instance.handlers
    )
    if not has_file_handler:
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(file_formatter)
        logger_instance.addHandler(file_handler)

    # Avoid duplicate StreamHandlers
    has_stream_handler = any(
        isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
        for h in logger_instance.handlers
    )
    if not has_stream_handler:
        stream_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level)
        stream_handler.setFormatter(stream_formatter)
        logger_instance.addHandler(stream_handler)

    return logger_instance


# Initialize singleton logger instance
logger = setup_logger()


def log_user_prompt(prompt: str, context: Optional[str] = None) -> None:
    """
    Logs prompts/queries submitted by the user.
    """
    tag = f" ({context})" if context else ""
    cleaned_prompt = prompt.strip() if isinstance(prompt, str) else str(prompt)
    logger.info(f"[USER PROMPT]{tag}: \"{cleaned_prompt}\"")


def log_agent_action(action: str, details: Optional[Any] = None) -> None:
    """
    Logs actions taken by the agent (e.g. state transitions, routing, node and tool executions).
    """
    if details is not None:
        logger.info(f"[AGENT ACTION] {action} | Details: {details}")
    else:
        logger.info(f"[AGENT ACTION] {action}")


def log_llm_timing(task: str, duration: float, model: Optional[str] = None) -> None:
    """
    Logs the time taken by an LLM to respond for a specific task.
    """
    model_str = f" | Model: {model}" if model else ""
    logger.info(f"[LLM TIME] Task: '{task}' | Latency: {duration:.3f}s{model_str}")


def log_agent_reasoning(subject: str, reasoning: str, details: Optional[Any] = None) -> None:
    """
    Logs reasoning performed by the agent or LLM (e.g. candidate evaluation, intent deduction).
    """
    cleaned_reasoning = reasoning.strip() if isinstance(reasoning, str) else str(reasoning)
    detail_str = f" | Details: {details}" if details is not None else ""
    logger.info(f"[AGENT REASONING] [{subject}] {cleaned_reasoning}{detail_str}")


def extract_content_text(content_raw: Any) -> str:
    """
    Helper to safely normalize response content into a clean string.
    Handles plain strings, list of text blocks, and dict representations.
    """
    if isinstance(content_raw, list):
        if content_raw and isinstance(content_raw[0], dict):
            return content_raw[0].get("text", "")
        elif content_raw:
            return str(content_raw[0])
        return ""
    return str(content_raw)


def extract_reasoning_metadata(response: Any) -> Optional[str]:
    """
    Extracts deep reasoning details if supplied by LLM providers (e.g. OpenRouter/DeepSeek reasoning).
    """
    # Check additional_kwargs
    additional = getattr(response, "additional_kwargs", {}) or {}
    if "reasoning" in additional and additional["reasoning"]:
        return str(additional["reasoning"])
    if "reasoning_details" in additional and additional["reasoning_details"]:
        return str(additional["reasoning_details"])

    # Check response_metadata
    metadata = getattr(response, "response_metadata", {}) or {}
    if "reasoning" in metadata and metadata["reasoning"]:
        return str(metadata["reasoning"])
    if "reasoning_details" in metadata and metadata["reasoning_details"]:
        return str(metadata["reasoning_details"])

    return None


def timed_llm_invoke(
    llm: Any,
    prompt: Any,
    task_name: str,
    extract_reasoning: bool = False,
    **kwargs: Any
) -> Tuple[Any, float, str]:
    """
    Executes an LLM invocation while tracking:
    1. Time taken to respond
    2. Extracted text content
    3. Reasonings (both explicit agent reasoning and provider-level reasoning tokens)

    Returns:
        (response_obj, elapsed_seconds, content_str)
    """
    start_time = time.perf_counter()
    try:
        response = llm.invoke(prompt, **kwargs)
        elapsed = time.perf_counter() - start_time
        content_str = extract_content_text(getattr(response, "content", response))
        
        # Log latency
        log_llm_timing(task_name, elapsed)

        # Log any provider-level reasoning tokens if present
        meta_reasoning = extract_reasoning_metadata(response)
        if meta_reasoning:
            log_agent_reasoning(f"{task_name} (Provider CoT)", meta_reasoning)

        # Log reasoning text if requested
        if extract_reasoning and content_str:
            log_agent_reasoning(task_name, content_str)

        return response, elapsed, content_str

    except Exception as e:
        elapsed = time.perf_counter() - start_time
        logger.error(f"[LLM ERROR] Task '{task_name}' failed after {elapsed:.3f}s: {e}")
        raise e
