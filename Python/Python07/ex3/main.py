from typing import Any
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


class DummyPlayer:
    def __init__(self, name: str):
        self.name = name
        self.health = 20


def main() -> None:
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    initial_battlefield = [DummyPlayer("Enemy Player")]
    engine = GameEngine(battlefield=initial_battlefield)

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    actions = engine.simulate_turn()

    hand_display = [f"{c.name} ({c.cost})" for c in engine.hand]
    print(f"Hand: {hand_display}")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {actions}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
