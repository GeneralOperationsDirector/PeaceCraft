import uuid
from peacecraft.database import save_session, load_session, delete_session
from peacecraft.config import DEFAULT_TRUST


def create_new_session(level: int = 1) -> dict:
    """Create a new session with default state."""
    session_id = str(uuid.uuid4())
    return {
        "session_id": session_id,
        "level": level,
        "npc_personality": None,
        "scenario": "",
        "trust_level": DEFAULT_TRUST,
        "conversation": [],
        "summary": ""
    }


def save_game_state(state: dict) -> None:
    """Save full session data to DB."""
    save_session(state["session_id"], state)


def load_game_state(session_id: str) -> dict | None:
    """Load existing session from DB."""
    return load_session(session_id)


def reset_session(session_id: str) -> None:
    """Delete a session entirely (for game over)."""
    delete_session(session_id)
