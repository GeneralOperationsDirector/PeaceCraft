# peacecraft/core/dialogue.py

from typing import List, Dict
import tiktoken

MAX_TOKENS = 2048


def estimate_tokens(text: str) -> int:
    # Simple word-based token estimate for now
    return len(text.split())


def summarize_dialogue(full_dialogue: List[Dict[str, str]]) -> str:
    # Naive summarization for now (could be replaced with LLM)
    summary = ""
    for turn in full_dialogue[:-5]:
        summary += f"{turn['role'].capitalize()}: {turn['text']}\n"
    return f"Summary of earlier conversation:\n{summary.strip()}"


def trim_dialogue(dialogue: List[Dict[str, str]]) -> List[Dict[str, str]]:
    running_text = "\n".join([f"{t['role']}: {t['text']}" for t in dialogue])
    if estimate_tokens(running_text) > MAX_TOKENS:
        summary = summarize_dialogue(dialogue)
        trimmed = dialogue[-5:]  # Keep last few exchanges
        return [{'role': 'system', 'text': summary}] + trimmed
    return dialogue


def format_dialogue_for_prompt(dialogue: List[Dict[str, str]]) -> str:
    return "\n".join([f"{turn['role'].capitalize()}: {turn['text']}" for turn in dialogue])
