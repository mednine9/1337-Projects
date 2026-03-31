from typing import Any
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        valid_effects = {"damage", "heal", "buff", "debuff"}
        if effect_type not in valid_effects:
            raise ValueError(f"Invalid effect type. Must be one of: {valid_effects}")
            
        self.effect_type = effect_type
        self.card_type = "Spell"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        player = game_state.get("player", {})
        
        if not self.is_playable(player.get("mana", 0)):
            return {"error": "Not enough mana"}
            
        player["mana"] -= self.cost
        
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Deal {self.cost} damage to target" if self.effect_type == "damage" else f"Apply {self.effect_type} effect"
        }

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        for target in targets:
            if self.effect_type == "damage" and hasattr(target, "health"):
                target.health -= self.cost
            elif self.effect_type == "heal" and hasattr(target, "health"):
                target.health += self.cost
            elif self.effect_type == "buff" and hasattr(target, "attack"):
                target.attack += self.cost
            elif self.effect_type == "debuff" and hasattr(target, "attack"):
                target.attack -= self.cost
                
        return {
            "effect_resolved": self.effect_type,
            "amount": self.cost
        }