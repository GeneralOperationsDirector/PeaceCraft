# peacecraft/game/game_loop.py

from peacecraft.core.scenario_generator import generate_scenario
from peacecraft.core.summarization import summarize_dialogue
from peacecraft.core.npc_response import get_npc_response
from peacecraft.core.database import save_session

from peacecraft.data.npc_personalities import get_random_npc

from typing import List
import uuid


def play_game():
    session_id = str(uuid.uuid4())
    level = 1
    story_summary = ""
    conversation: List[str] = []
    trust_level = 50

    print("\n" + "━" * 60)
    print("        🌍 WELCOME TO PEACECRAFT 🌍")
    print("━" * 60)
    print("Your mission is to de-escalate conflicts and achieve peaceful resolutions.")
    print("Each level presents a new challenge requiring negotiation and strategy.")
    print("NPC opponents will have distinct personalities that affect the difficulty.")
    print("━" * 60)

    while level <= 4:
        npc_profile = get_random_npc()
        print(f"\n🎭 Your opponent: {npc_profile['name']} ({npc_profile['type']})")

        scenario = generate_scenario(level, story_summary)
        print("\n" + "━" * 60)
        print(f"Level {level} - Scenario")
        print("━" * 60)
        print(scenario)

        while True:
            player_input = input("\n🗨️ Your response: ")
            if player_input.lower() in ("quit", "exit"):
                return

            conversation.append(f"Player: {player_input}")

            npc_response, sentiment_score, trust_change = get_npc_response(
                npc_profile, player_input, scenario, conversation, trust_level
            )

            trust_level += trust_change
            trust_level = max(0, min(100, trust_level))

            print(f"🧠 {npc_profile['name']}: {npc_response}")
            print(f"💙 Trust Level: {trust_level} | Sentiment Score: {sentiment_score}")

            conversation.append(f"{npc_profile['name']}: {npc_response}")

            if trust_level >= 70:
                print(
                    f"\n✅ Level {level} complete! You resolved the conflict peacefully."
                )
                break
            elif trust_level <= 20:
                print(f"\n❌ Level {level} failed. The conflict escalated.")
                break

        story_summary = summarize_dialogue(conversation)
        print("\n📘 Updated story summary:")
        print(story_summary)

        save_session(
            session_id,
            level,
            npc_profile,
            scenario,
            conversation,
            trust_level,
            story_summary,
        )

        level += 1

    print("\n🎉 Congratulations! You completed all 4 levels of Peacecraft.")


if __name__ == "__main__":
    play_game()
