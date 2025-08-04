# peacecraft/game.py

from peacecraft.game.loop import play_peacecraft_level
import random

from peacecraft.core.npc_profiles import NPC_PROFILES

NPC_PERSONALITIES = list(NPC_PROFILES.keys())


def start_game():
    print(
        """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        🌍 WELCOME TO PEACECRAFT 🌍
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your mission is to de-escalate conflicts and achieve peaceful resolutions.
Each level presents a new challenge requiring negotiation and strategy.
NPC opponents will have distinct personalities that affect the difficulty of resolving conflicts.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    )

    current_level = 1

    while True:
        npc_personality = random.choice(NPC_PERSONALITIES)
        print(
            f"Starting Level {current_level} against a(n) {npc_personality.title()} NPC..."
        )
        play_peacecraft_level(current_level, npc_personality)

        next_action = (
            input("Do you want to continue to the next level? (y/n): ").strip().lower()
        )
        if next_action != "y":
            print("Thanks for playing Peacecraft! 🌿")
            break

        current_level += 1


if __name__ == "__main__":
    start_game()
