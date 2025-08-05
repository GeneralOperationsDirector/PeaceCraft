#npc.py
from ollama import call_ollama_model
from config import OLLAMA_MODEL, MAX_HISTORY_ITEMS


def get_npc_response(npc_type, scenario, player_input, conversation_history=None):
    """
    Generates the NPC's response using the current model and inputs.
    """
    if conversation_history is None:
        conversation_history = []

    prompt = f"""
You are a {npc_type} NPC in a roleplaying game. The scenario is:

\"\"\"{scenario}\"\"\"

The player just said: "{player_input}"

Respond in character as a {npc_type}. Keep it brief and emotional if appropriate.
"""

    response = call_ollama_model(prompt, model=OLLAMA_MODEL)
    return response.strip()
