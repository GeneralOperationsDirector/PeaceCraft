from typing import List, Dict
from peacecraft.utils.ollama import generate_response


MAX_TOKENS = 2048

SUMMARIZATION_PROMPT = """
You are a summarizer for a conflict-resolution game called Peacecraft.

Summarize the following conversation into a short story recap.
Include:
- Key conflict themes
- Player's tone and approach (e.g., calm, assertive, empathetic)
- NPC behavior
- Outcome if it was resolved
- Trust level patterns if relevant

Keep the summary under 150 words.

Conversation:
{dialogue}
"""


def format_dialogue_for_prompt(dialogue: List[Dict[str, str]]) -> str:
    """Turn structured dialogue into plain text for LLM prompts."""
    return "\n".join(f"{msg['role'].capitalize()}: {msg['text']}" for msg in dialogue)


def estimate_tokens(text: str) -> int:
    """Rough estimate of token count based on words."""
    return len(text.split())


def summarize_dialogue(dialogue: List[Dict[str, str]]) -> str:
    """Send the conversation to Ollama and receive a summary."""
    formatted = format_dialogue_for_prompt(dialogue)
    prompt = SUMMARIZATION_PROMPT.format(dialogue=formatted)
    return generate_response(prompt)


def trim_dialogue(dialogue: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Trim old dialogue and prepend a summary if near token limit."""
    formatted = format_dialogue_for_prompt(dialogue)
    if estimate_tokens(formatted) > MAX_TOKENS:
        summary = summarize_dialogue(dialogue)
        return [{"role": "system", "text": summary}] + dialogue[-5:]
    return dialogue
