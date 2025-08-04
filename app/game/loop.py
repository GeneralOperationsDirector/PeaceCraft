# peacecraft/game/loop.py

from peacecraft.core.trust_engine import calculate_trust_change
from peacecraft.core.npc_profiles import get_npc_profile
from peacecraft.core.dialogue import generate_npc_response, generate_scenario


def play_peacecraft_level(level: int, npc_personality: str):
    trust_level = 50
    scenario = generate_scenario(level)

    print("\n🗺️ Scenario:")
    print(scenario)

    print("\n🤖 NPC Profile:")
    profile = get_npc_profile(npc_personality)
    print(f"Personality: {npc_personality.title()}\n")
    print(f"Description: {profile['description']}\n")

    conversation_history = []

    while True:
        player_input = input("\n🗨️ Your response: ").strip()
        conversation_history.append({"role": "player", "content": player_input})

        npc_response = generate_npc_response(
            npc_personality, player_input, scenario, conversation_history
        )
        conversation_history.append({"role": "npc", "content": npc_response})

        trust_delta = calculate_trust_change(npc_personality, player_input)
        trust_level += trust_delta
        trust_level = max(0, min(100, trust_level))

        print(f"\n🤖 NPC: {npc_response}")
        print(
            f"💙 Trust Level: {trust_level} ({'+' if trust_delta >= 0 else ''}{trust_delta})"
        )

        if trust_level >= 70:
            print("\n✅ Congratulations! You successfully de-escalated the situation.")
            print(f"✅ Level {level} complete! Moving to Level {level + 1}...\n")
            break
        elif trust_level <= 20:
            print("\n❌ The situation escalated. Try a different approach next time.")
            print(f"❌ Game over on Level {level}.\n")
            break
