import requests
import uuid
import json

def start_game():
    session_id = str(uuid.uuid4())
    level = input("Enter game level (1-4): ")
    
    response = requests.post(
        "http://localhost:8001/game/start",
        json={"session_id": session_id, "level": int(level)},
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 200:
        game_data = response.json()
        print(f"\nScenario: {game_data['scenario']}")
        play_game(session_id)
    else:
        print("Error starting game.")

def play_game(session_id):
    while True:
        player_input = input("\nYour response: ")
        if player_input.lower() == "exit":
            print("Exiting game...")
            break
        
        response = requests.post(
            "http://localhost:8001/game/respond",
            json={"session_id": session_id, "player_response": player_input},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            game_state = response.json()
            print(f"NPC: {game_state['npc_response']}")
            print(f"Trust Level: {game_state['trust_level']}")
            
            if game_state["game_status"] == "win":
                print("Congratulations! You resolved the conflict peacefully.")
                break
            elif game_state["game_status"] == "loss":
                print("Game over. The conflict escalated.")
                break
        else:
            print("Error processing response.")

if __name__ == "__main__":
    start_game()
