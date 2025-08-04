from pymongo import MongoClient
import os

# Connect to MongoDB (local instance)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["peacecraft"]  # Database name
sessions_collection = db["game_sessions"]  # Collection for storing game data

def save_game_session(session_id, level, npc_personality, scenario, trust_level, conversation):
    """ Save the current game session to MongoDB """
    session_data = {
        "session_id": session_id,
        "level": level,
        "npc_personality": npc_personality,
        "scenario": scenario,
        "trust_level": trust_level,
        "conversation": conversation
    }
    sessions_collection.update_one({"session_id": session_id}, {"$set": session_data}, upsert=True)

def load_game_session(session_id):
    """ Load an existing game session from MongoDB """
    return sessions_collection.find_one({"session_id": session_id})

def delete_game_session(session_id):
    """ Delete a game session """
    sessions_collection.delete_one({"session_id": session_id})

