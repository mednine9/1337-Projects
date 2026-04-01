import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures = {
            "dragon": {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary", "attack": 7, "health": 5},
            "goblin": {"name": "Goblin Warrior", "cost": 2, "rarity": "Common", "attack": 3, "health": 2}
        }
        self.spells = {
            "fireball": {"name": "Fireball", "cost": 4, "rarity": "Rare", "effect_type": "damage"},
            "lightning": {"name": "Lightning Bolt", "cost": 3, "rarity": "Common", "effect_type": "damage"}
        }
        self.artifacts = {
            "mana_ring": {"name": "Mana Ring", "cost": 2, "rarity": "Uncommon", "durability": 3, "effect": "+1 mana"}
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            data = random.choice(list(self.creatures.values()))

        elif isinstance(name_or_power, str):
            if name_or_power not in self.creatures:
                raise ValueError(f"Unknown creature name: {name_or_power}")
            data = self.creatures[name_or_power]

        elif isinstance(name_or_power, int):
            matching = [c for c in self.creatures.values() if c["attack"]
                        == name_or_power]
            if not matching:
                raise ValueError(
                    f"No creatures found with power level: {name_or_power}")
            data = random.choice(matching)

        else:
            raise TypeError("Invalid argument type for create_creature")

        return CreatureCard(data["name"], data["cost"], data["rarity"], data["attack"], data["health"])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            data = random.choice(list(self.spells.values()))

        elif isinstance(name_or_power, str):
            if name_or_power not in self.spells:
                raise ValueError(f"Unknown spell name: {name_or_power}")
            data = self.spells[name_or_power]

        elif isinstance(name_or_power, int):
            matching = [s for s in self.spells.values() if s["cost"]
                        == name_or_power]
            if not matching:
                raise ValueError(
                    f"No spells found with power level: {name_or_power}")
            data = random.choice(matching)

        else:
            raise TypeError("Invalid argument type for create_spell")

        return SpellCard(data["name"], data["cost"], data["rarity"], data["effect_type"])

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            data = random.choice(list(self.artifacts.values()))

        elif isinstance(name_or_power, str):
            if name_or_power not in self.artifacts:
                raise ValueError(f"Unknown artifact name: {name_or_power}")
            data = self.artifacts[name_or_power]

        elif isinstance(name_or_power, int):
            matching = [a for a in self.artifacts.values() if a["cost"]
                        == name_or_power]
            if not matching:
                raise ValueError(
                    f"No artifacts found with power level: {name_or_power}")
            data = random.choice(matching)

        else:
            raise TypeError("Invalid argument type for create_artifact")

        return ArtifactCard(data["name"], data["cost"], data["rarity"], data["durability"], data["effect"])

    def create_themed_deck(self, size: int) -> dict[str, list[Card]]:
        deck: dict[str, list[Card]] = {
            "creatures": [], "spells": [], "artifacts": []}

        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])

            if card_type == "creature":
                deck["creatures"].append(self.create_creature())
            elif card_type == "spell":
                deck["spells"].append(self.create_spell())
            else:
                deck["artifacts"].append(self.create_artifact())

        return deck

    def get_supported_types(self) -> dict[str, list[str]]:
        return {
            "creatures": list(self.creatures.keys()),
            "spells": list(self.spells.keys()),
            "artifacts": list(self.artifacts.keys())
        }
