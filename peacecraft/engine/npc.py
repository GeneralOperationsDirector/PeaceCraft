from peacecraft.utils.ollama import generate_response

# In-memory memory storage (can later be moved to DB if needed)
npc_memory = {}

# Static personality traits (can later move to a JSON/YAML config)
NPC_PERSONALITIES = {
    "aggressive": "Quick to anger, confrontational, and blunt. Escalates easily if challenged.",
    "skeptical": "Distrustful of motives and intentions. Questions everything.",
    "emotional": "Highly reactive and emotionally driven. Responds to tone more than logic.",
    "manipulative": "Twists words and tries to control the conversation through guilt or deception.",
    "stubborn": "Unwilling to compromise. Values control and consistency.",
}


PROMPT_TEMPLATE = """
You are an NPC in a negotiation-based game called Peacecraft.

Conflict Scenario:
{scenario}

Your Personality:
{npc_personality} - {personality_desc}

Conversation So Far:
{conversation_history}

The player now says:
"{player_input}"

Respond in character:
- Stay true to your personality
- Escalate or de-escalate based on the player's tone and content
- Keep your responses natural, human, and emotionally consistent
"""


def get_npc_response(session_id: str, npc_personality: str, scenario: str, player_input: str) -> str:
    """Generate an NPC response based on the session context and latest player input."""
    
    if session_id not in npc_memory:
        npc_memory[session_id] = []

    memory = npc_memory[session_id][-5:]  # Limit memory to last 5 lines
    conversation_history = "\n".join(memory)

    prompt = PROMPT_TEMPLATE.format(
        scenario=scenario,
        npc_personality=npc_personality,
        personality_desc=NPC_PERSONALITIES.get(npc_personality.lower(), "neutral"),
        conversation_history=conversation_history,
        player_input=player_input,
    )

    response = generate_response(prompt)

    # Update memory
    npc_memory[session_id].append(f"Player: {player_input}")
    npc_memory[session_id].append(f"NPC: {response}")

    return response
