#main.py
import uuid
import argparse
from config import DEFAULT_TRUST, MAX_LEVEL, MAX_HISTORY_ITEMS
from scenario import generate_scenario
from trust import analyze_trust_shift
from npc import get_npc_response
from database import log_conversation_chunk
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
        player_input = input("🗨️ Your response (type 'say:' or 'do:'): ").strip()
        if player_input.lower() in ["exit", "quit", "say: exit", "do: exit", "say: quit", "do: quit"]:
            print("\n👋 Exiting Peacecraft. Until next time!")
            break

        conversation_history.append({"role": "player", "text": player_input})

        npc_reply = get_npc_response(
            npc_type=npc_type,
            scenario=scenario,
            player_input=player_input
        )

        print(f"\n🤖 NPC: {npc_reply}")
        conversation_history.append({"role": "npc", "text": npc_reply})

        trust = analyze_trust_shift(session_id, npc_type, trust, conversation_history)
        print(f"💙 Trust Level: {trust}\n")

        summary = summarize_conversation(conversation_history[-MAX_HISTORY_ITEMS:])
        print(f"🧠 Memory Saved for RAG:  {summary}\n")
        log_conversation_chunk(session_id, npc_type, conversation_history[-MAX_HISTORY_ITEMS:], summary)


def main():
    parser = argparse.ArgumentParser(description="Start Peacecraft with a given level.")
    parser.add_argument("--level", type=int, default=1, help="Conflict level (1-4)")
    args = parser.parse_args()

    if args.level < 1 or args.level > MAX_LEVEL:
        print(f"Invalid level: {args.level}. Please choose a level between 1 and {MAX_LEVEL}.")
    else:
        run_game_loop(args.level)


if __name__ == "__main__":
    main()
