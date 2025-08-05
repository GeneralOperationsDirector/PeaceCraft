#mediator.py
from ollama import call_ollama_model  # or however your Ollama call is structured

def analyze_trust_with_mediator(session_id, npc_type, trust_before, conversation_history):
    recent_dialogue = conversation_history[-4:]
    
    prompt = {
        "system": "You are a conflict mediator assessing conversations between a player and an NPC. Based on the interaction, suggest how trust should be adjusted.",
        "user": f"NPC Type: {npc_type}\nTrust Before: {trust_before}\nRecent Dialogue:\n" +
                "\n".join([f"{msg['role']}: {msg['text']}" for msg in recent_dialogue])
    }

    result = call_ollama_model(prompt)  # You'll implement this
    parsed = parse_response(result)  # e.g., {"trust_change": -5, "summary": "..."}
    
    trust_after = max(0, min(100, trust_before + parsed["trust_change"]))
    log_trust_adjustment(session_id, npc_type, trust_before, trust_after, parsed["summary"])

    return trust_after
