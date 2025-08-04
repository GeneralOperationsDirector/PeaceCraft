from peacecraft.engine.trust import analyze_sentiment, adjust_trust_level
from peacecraft.engine.npc import get_npc_response
from peacecraft.engine.scenario import generate_scenario
from peacecraft.engine.dialogue import summarize_dialogue
from peacecraft.engine.session import (
    create_new_session,
    load_game_state,
    save_game_state,
    reset_session,
)
from peacecraft.config import TRUST_WIN_THRESHOLD, TRUST_LOSS_THRESHOLD, MAX_LEVEL

import random


def play_level(state: dict) -> str:
    """Run a single level of the game, return result: 'win', 'loss', or 'quit'"""
    print(f"\n🎭 NPC Personality: {state['npc_personality']}")
    print(f"\n📖 Scenario:\n{state['scenario']}")
    print(f"\n💙 Starting Trust Level: {state['trust_level']}")

    while True:
        player_input = input("\n🗨️ Your response: ").strip()
        if player_input.lower() in ("exit", "quit"):
            return "quit"

        sentiment = analyze_sentiment(player_input)
        state["trust_level"] = adjust_trust_level(
            state["trust_level"], sentiment, state["npc_personality"]
        )

        npc_reply = get_npc_response(
            state["session_id"],
            state["npc_personality"],
            state["scenario"],
            player_input,
        )

        state["conversation"].append({"role": "player", "text": player_input})
        state["conversation"].append({"role": "npc", "text": npc_reply})

        print(f"\n🤖 NPC: {npc_reply}")
        print(f"💙 Trust Level: {state['trust_level']}")

        if state["trust_level"] >= TRUST_WIN_THRESHOLD:
            print("\n✅ You peacefully resolved the conflict!")
            return "win"
        elif state["trust_level"] <= TRUST_LOSS_THRESHOLD:
            print("\n❌ The conflict escalated beyond control.")
            return "loss"


def main():
    print("\n" + "━" * 60)
    print("        🌍 WELCOME TO PEACECRAFT 🌍")
    print("━" * 60)
    print("Negotiate your way through escalating levels of conflict.")
    print("Type 'exit' anytime to quit.\n")

    state = create_new_session()
    level = state["level"]

    while level <= MAX_LEVEL:
        state["npc_personality"] = random.choice(
            ["aggressive", "skeptical", "emotional", "manipulative", "stubborn"]
        )

        state["scenario"] = generate_scenario(level, story_summary=state["summary"])
        state["trust_level"] = 50
        state["conversation"] = []

        save_game_state(state)

        result = play_level(state)

        if result == "win":
            state["summary"] = summarize_dialogue(state["conversation"])
            level += 1
            state["level"] = level
            print(f"\n📘 Updated Summary:\n{state['summary']}")
            save_game_state(state)
        elif result == "loss":
            reset_session(state["session_id"])
            print("\n🔄 Restarting from Level 1...")
            state = create_new_session()
            level = 1
        elif result == "quit":
            print("\n👋 Game ended. See you next time!")
            break

    if level > MAX_LEVEL:
        print("\n🎉 You completed all levels of Peacecraft! 🕊️")
        reset_session(state["session_id"])


if __name__ == "__main__":
    main()
