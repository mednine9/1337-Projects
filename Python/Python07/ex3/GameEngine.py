import random
from typing import Any
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self, battlefield: list[Any] | None = None) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hand: list[Any] = []
        self.battlefield: list[Any] = battlefield if battlefield is not None else [
        ]

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        if not self.factory or not self.strategy:
            raise RuntimeError("Engine not configured")

        types = ["creatures", "spells", "artifacts"]
        for _ in range(3):
            choice = random.choice(types)
            if choice == "creatures":
                card = self.factory.create_creature()
            elif choice == "spells":
                card = self.factory.create_spell()
            else:
                card = self.factory.create_artifact()

            self.hand.append(card)
            self.cards_created += 1

        self.turns_simulated += 1

        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.total_damage += actions.get("damage_dealt", 0)

        return actions

    def get_engine_status(self) -> dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name() if self.strategy else "None",
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
