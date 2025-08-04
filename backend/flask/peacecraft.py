from flask import Flask, render_template, request, jsonify
import requests
import uuid
import json

app = Flask(__name__)
API_BASE_URL = "http://localhost:8000"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start_game", methods=["POST"])
def start_game():
    session_id = str(uuid.uuid4())
    level = request.json.get("level", 1)  # Ensure JSON parsing

    request_data = {"session_id": session_id, "level": level}
    print(
        f"Sending request to FastAPI: {json.dumps(request_data, indent=4)}"
    )  # Debugging output

    response = requests.post(
        f"{API_BASE_URL}/game/start",
        json=request_data,
        headers={"Content-Type": "application/json"},
    )

    print(
        f"Response from FastAPI: {response.status_code}, {response.text}"
    )  # Debugging output

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error starting game"}), 500


@app.route("/send_response", methods=["POST"])
def send_response():
    data = request.json
    response = requests.post(
        f"{API_BASE_URL}/game/respond",
        json={
            "session_id": data["session_id"],
            "player_response": data["player_response"],
        },
        headers={"Content-Type": "application/json"},
    )

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error processing response"}), 500


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
