from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
import uuid
import json

app = FastAPI()

# Temporary in-memory storage (replace with DB later)
sessions = {}
LOG_FILE = "game_log.json"


class PlayerInput(BaseModel):
    session_id: str
    player_response: str


# NPC Personalities
NPC_PERSONALITIES = {
    "aggressive": "Responds harshly, quick to escalate.",
    "skeptic": "Doubts every statement, needs convincing.",
    "emotional": "Highly reactive, responds to tone more than logic.",
    "manipulative": "Twists words and tries to gain the upper hand.",
    "stubborn": "Very resistant to change, hard to persuade.",
}

# Trust level thresholds
TRUST_WIN = 80
TRUST_LOSS = 20


def save_log(data):
    """Save game state to a log file"""
    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(data, indent=4) + "\n")


@app.post("/game/start")
def start_game(session_id: str):
    if session_id in sessions:
        raise HTTPException(status_code=400, detail="Session ID already exists")

    npc_personality = uuid.uuid4().hex[:10]  # Random selection for now
    trust_level = 50  # Start at neutral trust
    scenario = "A person cuts in line at a store. How does the player handle it?"

    sessions[session_id] = {
        "npc_personality": npc_personality,
        "trust_level": trust_level,
        "conversation": [{"role": "npc", "text": scenario}],
    }

    log_data = {
        "event": "game_started",
        "session_id": session_id,
        "npc_personality": npc_personality,
        "trust_level": trust_level,
        "scenario": scenario,
    }
    save_log(log_data)

    return {
        "scenario": scenario,
        "npc_personality": npc_personality,
        "trust_level": trust_level,
    }


@app.post("/game/respond")
def process_response(player_input: PlayerInput):
    session = sessions.get(player_input.session_id)
    if not session:
        raise HTTPException(status_code=400, detail="Invalid session ID")

    # Append player response to history
    session["conversation"].append(
        {"role": "player", "text": player_input.player_response}
    )

    # Generate NPC response using Ollama
    npc_prompt = f"NPC Personality: {NPC_PERSONALITIES.get(session['npc_personality'], 'neutral')}\n"
    npc_prompt += "Previous conversation: " + " | ".join(
        [msg["text"] for msg in session["conversation"]]
    )
    npc_prompt += (
        f"\nPlayer said: {player_input.player_response}\nHow does the NPC respond?"
    )

    # Debugging logs
    print(f"Sending to Ollama:\nModel: mistral\nPrompt:\n{npc_prompt}")

    try:
        ollama_response = ollama.generate(model="mistral", prompt=npc_prompt)
        npc_response = ollama_response.response  # Extract only the text response
        print(f"Ollama Response: {npc_response}")
    except Exception as e:
        print(f"Error calling Ollama: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Ollama error: {str(e)}")

    session["conversation"].append({"role": "npc", "text": npc_response})

    # Adjust trust level based on player response (simplified logic)
    if "calm" in player_input.player_response.lower():
        session["trust_level"] += 10
    elif "angry" in player_input.player_response.lower():
        session["trust_level"] -= 10

    log_data = {
        "event": "player_response",
        "session_id": player_input.session_id,
        "player_response": player_input.player_response,
        "npc_response": npc_response,  # Now only storing the actual text
        "trust_level": session["trust_level"],
    }
    save_log(log_data)

    # Determine game status
    if session["trust_level"] >= TRUST_WIN:
        return {
            "npc_response": npc_response,
            "trust_level": session["trust_level"],
            "game_status": "win",
        }
    elif session["trust_level"] <= TRUST_LOSS:
        return {
            "npc_response": npc_response,
            "trust_level": session["trust_level"],
            "game_status": "loss",
        }

    return {
        "npc_response": npc_response,
        "trust_level": session["trust_level"],
        "game_status": "ongoing",
    }


@app.get("/game/state")
def get_game_state(session_id: str):
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=400, detail="Invalid session ID")

    return session
