# database.py
from datetime import datetime
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME, DIALOGUE_COLLECTION

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
trust_log_collection = db["trust_logs"]

def log_trust_adjustment(session_id, npc_type, trust_before, trust_after, summary):
    log = {
        "session_id": session_id,
        "npc_type": npc_type,
        "trust_before": trust_before,
        "trust_after": trust_after,
        "adjustment": trust_after - trust_before,
        "summary": summary
    }
    trust_log_collection.insert_one(log)

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
