from typing import Any
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers")
        
        self.attack = attack
        self.health = health
        self.type = "Creature"

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
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: "CreatureCard") -> dict[str, Any]:
        initial_health = target.health
        target.health -= self.attack
        
        damage_dealt = self.attack
        if target.health < 0:
            damage_dealt = initial_health
            target.health = 0
            
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage_dealt,
            "combat_resolved": target.health == 0
        }