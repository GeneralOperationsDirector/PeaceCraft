from pymongo import MongoClient
from peacecraft.config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
sessions = db[COLLECTION_NAME]


def save_session(session_id: str, data: dict) -> None:
    """Save or update a game session."""
    sessions.update_one({"session_id": session_id}, {"$set": data}, upsert=True)


def load_session(session_id: str) -> dict | None:
    """Load an existing game session."""
    return sessions.find_one({"session_id": session_id})


def delete_session(session_id: str) -> None:
    """Delete a saved game session."""
    sessions.delete_one({"session_id": session_id})
