# peacecraft/core/summarization.py

import requests
from typing import List

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral-nemo"

SUMMARIZATION_PROMPT_TEMPLATE = """
You are an expert summarizer for an interactive RPG game called Peacecraft.
The game follows a player through escalating levels of conflict.

Your job is to condense the previous dialogue and outcomes into a short story summary.
This summary will be used in future levels to help the AI understand what has happened before.

Include:
- Key conflict themes
- Major NPCs and their behavior
- Resolution method (if applicable)
- Tone and approach of the player (e.g., diplomatic, firm, empathetic)
- Trust level trends if relevant

Keep it concise (150 words max).

Here is the game history:

{dialogue_history}

Now, generate a summary:
"""


def summarize_dialogue(dialogue_history: List[str]) -> str:
    joined_history = "\n".join(dialogue_history)
    prompt = SUMMARIZATION_PROMPT_TEMPLATE.format(dialogue_history=joined_history)

    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json().get("response", "[No summary generated]")
