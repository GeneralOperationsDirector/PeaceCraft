import uuid
import argparse

from scenario import generate_scenario
from trust import adjust_trust_level
from npc import get_npc_response
from database import log_conversation_chunk
from config import DEFAULT_TRUST, MAX_HISTORY_ITEMS
from summarization import summarize_conversation 


def run_game_loop(level):
    session_id = str(uuid.uuid4())
    npc_by_level = {
        1: "aggressor",
        2: "manipulator",
        3: "emotional",
        4: "warmonger"
    }
    npc_type = npc_by_level.get(level, "neutral")

    scenario = generate_scenario(level)
    trust = DEFAULT_TRUST
    conversation_history = []

    print("\n" + "━" * 60)
    print("        🌍 WELCOME TO PEACECRAFT 🌍")
    print("━" * 60)
    print("Negotiate your way through escalating levels of conflict.")
    print("Type 'exit' anytime to quit.\n")
    print(f"🎭 NPC Personality: {npc_type}\n")
    print("📖 Scenario:")
    print(scenario)
    print(f"\n💙 Starting Trust Level: {trust}\n")

    while True:
        player_input = input("🗨️ Your response: ")
        if player_input.lower() in ["exit", "quit"]:
            print("\n👋 Exiting Peacecraft. Until next time!")
            break

        conversation_history.append({"role": "player", "text": player_input})

        npc_reply = get_npc_response(
            npc_type=npc_type,
            scenario=scenario,
            player_input=player_input,
            conversation_history=conversation_history
        )

        print(f"\n🤖 NPC: {npc_reply}")
        conversation_history.append({"role": "npc", "text": npc_reply})

        trust = adjust_trust_level(trust, npc_reply)
        print(f"💙 Trust Level: {trust}\n")

        # RAG logging
        summary = summarize_conversation(conversation_history[-MAX_HISTORY_ITEMS:])

        log_conversation_chunk(
            session_id=session_id,
            npc_type=npc_type,
            conversation=conversation_history[-MAX_HISTORY_ITEMS:],
            summary=summary
        )
        print(f"🧠 Memory Saved for RAG: {summary}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start Peacecraft with a given level.")
    parser.add_argument("--level", type=int, default=1, help="Conflict level (1-4)")
    args = parser.parse_args()
    run_game_loop(args.level)
