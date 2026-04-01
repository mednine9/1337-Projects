from typing import Any
from ex0.Card import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        def sort_targets(target: Any) -> float:
            name = getattr(target, "name", "").lower()
            if "player" in name:
                return -1.0
            return float(getattr(target, "health", 999))

        return sorted(available_targets, key=sort_targets)

    def execute_turn(self, hand: list[Card], battlefield: list[Any]) -> dict[str, Any]:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = []

        sorted_hand = sorted(hand, key=lambda c: getattr(c, "cost", 999))
        attackers = []

        for card in sorted_hand:
            if mana_used + getattr(card, "cost", 0) <= 5:
                cards_played.append(card.name)
                mana_used += getattr(card, "cost", 0)

                if hasattr(card, "attack") or getattr(card, "effect_type", "") == "damage":
                    attackers.append(card)

        targets = self.prioritize_targets(battlefield)

        for attacker in attackers:
            if not targets:
                break

            target = targets[0]
            target_name = getattr(target, "name", "Unknown Target")

            attack_power = getattr(
                attacker, "attack", getattr(attacker, "cost", 0))

            if target_name not in targets_attacked:
                targets_attacked.append(target_name)

            damage_dealt += attack_power

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }
