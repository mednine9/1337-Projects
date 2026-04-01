from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        defense: int,
        health: int,
        mana: int
    ) -> None:
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.defense = defense
        self.health = health
        self.mana = mana
        self.card_type = "Elite"

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
            "effect": "Elite summoned to battlefield"
        }

    def attack(self, target: Any) -> dict[str, Any]:
        damage = self.attack_power
        target_name = getattr(target, "name", str(target))

        if hasattr(target, "health"):
            target.health -= damage

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": damage,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list[Any]) -> dict[str, Any]:
        spell_cost = 4
        if self.mana < spell_cost:
            return {"error": "Not enough mana"}

        self.mana -= spell_cost
        target_names = [getattr(t, "name", str(t)) for t in targets]

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": target_names,
            "mana_used": spell_cost
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "mana": self.mana
        }
