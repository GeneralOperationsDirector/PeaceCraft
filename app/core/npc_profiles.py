# peacecraft/core/npc_profiles.py

NPC_PROFILES = {
    "aggressive": {
        "description": "Quick to anger, confrontational, and blunt. This NPC escalates easily if challenged.",
        "how_to_win": "Remain calm and assertive. Use nonviolent communication and show empathy without backing down.",
        "how_to_lose": "React with aggression, sarcasm, or dismissive behavior. Raising your voice increases hostility."
    },
    "manipulative": {
        "description": "Twists words and tries to control the situation. This NPC uses guilt, persuasion, or misinformation.",
        "how_to_win": "Stay logical and question inconsistencies. Remain focused on facts and set clear boundaries.",
        "how_to_lose": "Fall for emotional traps or vague reasoning. Letting them lead the discussion blindly will backfire."
    },
    "emotional": {
        "description": "Highly reactive and emotionally driven. This NPC may cry, yell, or withdraw easily.",
        "how_to_win": "Validate their feelings and speak gently. Avoid logic-heavy responses early on.",
        "how_to_lose": "Ignore their emotions or be too blunt. Overanalyzing or dismissing their experience is harmful."
    },
    "skeptical": {
        "description": "Distrustful of motives and intentions. Questions everything and expects to be disappointed.",
        "how_to_win": "Be transparent and consistent. Offer examples and follow through on promises.",
        "how_to_lose": "Be vague or overpromise. Any dishonesty or contradiction fuels their doubt."
    },
    "stubborn": {
        "description": "Unwilling to change their mind or compromise. Feels safest when in control.",
        "how_to_win": "Offer choices instead of ultimatums. Help them feel like a decision-maker in the resolution.",
        "how_to_lose": "Force change or issue demands. Making them feel out of control hardens their resistance."
    }
}


def get_npc_profile(personality: str) -> dict:
    return NPC_PROFILES.get(personality, {})
