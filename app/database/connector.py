# peacecraft/database/connector.py

from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "peacecraft"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
game_sessions = db["game_sessions"]
