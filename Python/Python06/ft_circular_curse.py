import alchemy.grimoire as grimoire
from alchemy.grimoire.validator import validate_ingredients


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nMethod 1: Testing late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): "
          f"{grimoire.record_spell('Lightning', 'air')}")

    print("\nMethod 2: Testing dependency injection technique:")
    injection_result = grimoire.spellbook.record_spell_injected(
        "Earthquake", "earth", validate_ingredients
    )
    print(
        "record_spell_injected(\"Earthquake\", "
        "\"earth\", validate_ingredients): "
        f"{injection_result}"
    )

    print("\nCircular dependency curse avoided using multiple techniques!")


if __name__ == "__main__":
    main()
