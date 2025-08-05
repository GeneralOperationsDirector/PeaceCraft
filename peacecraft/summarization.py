#summarization.py
from ollama import call_ollama_model
from config import OLLAMA_MODEL


def summarize_conversation(conversation_history):
    dialogue = "\n".join([f"{entry['role']}: {entry['text']}" for entry in conversation_history])
    prompt = f"""
Summarize the following conversation between a player and an NPC in one or two sentences:

{dialogue}
"""
    return call_ollama_model(prompt, model=OLLAMA_MODEL)
