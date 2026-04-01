from typing import Any
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    dragon_info = dragon.get_card_info()
    dragon_info["type"] = dragon.type
    dragon_info["attack"] = dragon.attack
    dragon_info["health"] = dragon.health

    print("CreatureCard Info:")
    print(dragon_info)

    game_state: dict[str, Any] = {
        "player": {"mana": 6},
        "battlefield": []
    }

    mana = game_state["player"]["mana"]
    print(f"\nPlaying {dragon.name} with {mana} mana available:")
    print(f"Playable: {dragon.is_playable(mana)}")
    print(f"Play result: {dragon.play(game_state)}")

    goblin = CreatureCard(
        name="Goblin Warrior",
        cost=2,
        rarity="Common",
        attack=3,
        health=2
    )

    print(f"\n{dragon.name} attacks {goblin.name}:")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    game_state["player"]["mana"] = 3
    mana = game_state["player"]["mana"]
    print(f"\nTesting insufficient mana ({mana} available):")
    print(f"Playable: {dragon.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
