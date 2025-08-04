# peacecraft/core/prompts.py

from typing import Literal

NPCPersonality = Literal["aggressive", "skeptical", "emotional", "manipulative", "stubborn"]


def build_scenario_prompt(level: int) -> str:
    return f"""
You are a scenario designer for a peaceful conflict resolution RPG.
Generate a level {level} scenario involving a one-on-one conflict.
Keep the situation appropriate to the level (e.g., simple disagreement at level 1, complex negotiation at level 4).
Include:
- A clear title
- A short setting description
- The roles of both characters
- The core conflict
- The goal for the player
    """.strip()


def build_npc_prompt(personality: NPCPersonality, trust_level: int, dialogue: str) -> str:
    return f"""
You are an NPC in a game called Peacecraft. Your personality is: {personality}.
Trust level toward the player is currently: {trust_level}.
Respond as if you're in a conflict with the player, based on the following dialogue history:

{dialogue}

Respond as your character would naturally respond in this situation.
    """.strip()
