# database.py
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME, DIALOGUE_COLLECTION

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
sessions = db[COLLECTION_NAME]
dialogue_collection = db[DIALOGUE_COLLECTION]

def save_session(session_id, data):
    sessions.update_one({"session_id": session_id}, {"$set": data}, upsert=True)

def log_conversation_chunk(session_id, npc_type, conversation, summary):
    dialogue_collection.insert_one({
        "session_id": session_id,
        "npc_type": npc_type,
        "conversation": conversation,
        "summary": summary,
    })

def find_similar_conversations(session_id, npc_type, limit=5):
    return list(dialogue_collection.find({
        "npc_type": npc_type,
        "session_id": {"$ne": session_id}
    }).sort("_id", -1).limit(limit))
