# peacecraft/core/scenario_generator.py

import requests

PROMPT_TEMPLATE = """
You are a dynamic conflict scenario generator for a game called Peacecraft.
The player experiences an unfolding story across four escalating levels of conflict:

Level 1 - Personal: Focus on emotional intelligence and communication. The player faces common social tensions, like someone cutting in line or invading personal space.
Level 2 - Ideological: Test the player's ability to handle values-based disagreement, including political debates, social ideologies, or business negotiations.
Level 3 - Institutional: The player must mediate structured disputes between groups or within organizations—resolving rules, rights, or legal questions.
Level 4+ - Global: The final challenges are about diplomacy and global crises—nations at odds, trade wars, military de-escalation.

The player progresses from everyday life into positions of influence and power, and must resolve conflicts peacefully at each stage.

Instructions:
Generate a dynamic and richly described scenario for Level {level} that feels like a chapter in a continuing story. Include:
- A brief Title
- A specific Setting (geographical, social, or institutional)
- A compelling Conflict description with emotional or political tension
- Two Characters: the Player and a named NPC with a distinct role
- A Goal for the player that requires peaceful resolution

Ensure the conflict suits the level and evolves with the narrative. Do not resolve the conflict—leave that to the player.
"""

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral-nemo"


def generate_scenario(level: int, story_summary: str = "") -> str:
    # Build context-aware prompt
    if story_summary:
        context = f"Previous Story Summary:\n{story_summary}\n\n"
    else:
        context = ""

    prompt = context + PROMPT_TEMPLATE.format(level=level)
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json().get("response", "[No scenario generated]")
