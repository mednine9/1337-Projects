from typing import Any
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity:
        str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability < 0:
            raise ValueError("Durability cannot be negative")

        self.durability = durability
        self.effect = effect
        self.card_type = "Artifact"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        player = game_state.get("player", {})

        if not self.is_playable(player.get("mana", 0)):
            return {"error": "Not enough mana"}

        player["mana"] -= self.cost

        if "battlefield" in game_state:
            game_state["battlefield"].append(self)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict[str, Any]:
        if self.durability <= 0:
            return {"error": "Artifact destroyed"}

        self.durability -= 1

        return {
            "artifact": self.name,
            "remaining_durability": self.durability,
            "effect": self.effect
        }
