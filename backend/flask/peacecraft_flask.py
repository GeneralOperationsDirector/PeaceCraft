from flask import Flask, render_template, request, jsonify
import requests
import uuid

app = Flask(__name__)
API_BASE_URL = "http://localhost:8001"

# Store conversation history in memory (temporary solution, can be improved with DB)
conversations = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start_game", methods=["POST"])
def start_game():
    session_id = str(uuid.uuid4())
    response = requests.post(f"{API_BASE_URL}/game/start?session_id={session_id}")

    if response.status_code == 200:
        scenario = response.json().get("scenario", "Unexpected response")
        conversations[session_id] = [{"role": "npc", "text": scenario}]
        return jsonify(
            {
                "session_id": session_id,
                "scenario": scenario,
                "trust_level": 50,
                "conversation": conversations[session_id],
            }
        )
    else:
        return jsonify({"error": "Error starting game"}), 500


@app.route("/send_response", methods=["POST"])
def send_response():
    data = request.json
    print(f"Received data: {data}")  # Debugging log

    if not data or "session_id" not in data or "player_response" not in data:
        return jsonify({"error": "Missing session_id or player_response"}), 400

    session_id = data["session_id"].strip()
    player_response = data["player_response"].strip()

    if not session_id or not player_response:
        return jsonify({"error": "session_id and player_response cannot be empty"}), 400

    payload = {"session_id": session_id, "player_response": player_response}
    print(f"Sending to backend: {payload}")  # Debugging log

    response = requests.post(
        f"{API_BASE_URL}/game/respond",
        json=payload,
        headers={"Content-Type": "application/json"},
    )

    print(f"Backend response: {response.status_code}, {response.text}")  # Debugging log

    if response.status_code == 200:
        response_data = response.json()
        npc_response = response_data.get("npc_response", "NPC has no response.")
        trust_level = response_data.get("trust_level", 50)

        # Append to conversation history
        if session_id in conversations:
            conversations[session_id].append(
                {"role": "player", "text": player_response}
            )
            conversations[session_id].append({"role": "npc", "text": npc_response})
        else:
            conversations[session_id] = [
                {"role": "player", "text": player_response},
                {"role": "npc", "text": npc_response},
            ]

        return jsonify(
            {
                "npc_response": npc_response,
                "trust_level": trust_level,
                "conversation": conversations[session_id],
            }
        )
    else:
        return (
            jsonify({"error": f"Error processing response: {response.text}"}),
            response.status_code,
        )


@app.route("/game_state", methods=["GET"])
def get_game_state():
    session_id = request.args.get("session_id")
    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    response = requests.get(f"{API_BASE_URL}/game/state?session_id={session_id}")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error retrieving game state"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
