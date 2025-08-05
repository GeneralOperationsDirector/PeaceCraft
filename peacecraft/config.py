#config.py
import os

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "peacecraft"
COLLECTION_NAME = "game_sessions"

# Ollama
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_MEDIATOR_MODEL = os.getenv("OLLAMA_MEDIATOR_MODEL", OLLAMA_MODEL)

# Game Settings
DEFAULT_TRUST = 50
TRUST_WIN_THRESHOLD = 70
TRUST_LOSS_THRESHOLD = 25
MAX_LEVEL = 4
MAX_HISTORY_ITEMS = 6
DIALOGUE_COLLECTION = "npc_dialogues"
