# peacecraft/database/crud.py

from peacecraft.database.connector import game_sessions
from datetime import datetime


def save_game_session(
    session_id: str,
    level: int,
    npc_personality: dict,
    scenario: str,
    conversation: list,
    trust_level: int,
    story_summary: str,
):
    doc = {
        "session_id": session_id,
        "level": level,
        "npc_personality": npc_personality,
        "scenario": scenario,
        "conversation": conversation,
        "trust_level": trust_level,
        "story_summary": story_summary,
        "status": "in_progress",
        "timestamp": datetime.utcnow(),
    }
    game_sessions.insert_one(doc)


def update_game_session(session_id: str, trust_level: int, conversation: list):
    game_sessions.update_one(
        {"session_id": session_id},
        {
            "$set": {
                "trust_level": trust_level,
                "conversation": conversation,
                "last_updated": datetime.utcnow(),
            }
        },
    )


def get_game_session(session_id: str):
    return game_sessions.find_one({"session_id": session_id})
