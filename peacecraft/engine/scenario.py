from peacecraft.utils.ollama import generate_response

PROMPT_TEMPLATE = """
You are a dynamic conflict scenario generator for a game called Peacecraft.
The player experiences an unfolding story across escalating levels of conflict:

Level 1 - Personal: Emotional or social tension (e.g., being disrespected in public).
Level 2 - Ideological: Conflict rooted in values or beliefs.
Level 3 - Institutional: Disputes within or between organizations.
Level 4 - Global: International or geopolitical crises.

Generate a scenario for Level {level} that includes:
- A short Title
- Setting (e.g., workplace, family, political meeting)
- Conflict summary (2-3 sentences)
- Two characters: the Player and a named NPC
- A peaceful goal the Player should try to achieve

Make it engaging and leave the resolution to the player.
{story_summary}
"""


def generate_scenario(level: int, story_summary: str = "") -> str:
    """Generate a scenario based on the level and optional story context."""
    summary = f"\nPrevious summary:\n{story_summary.strip()}" if story_summary else ""
    prompt = PROMPT_TEMPLATE.format(level=level, story_summary=summary)
    return generate_response(prompt)
