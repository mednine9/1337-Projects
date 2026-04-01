from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    card_methods = [x for x in dir(Card) if not x.startswith('_')]
    print(f"Card: {card_methods}")

    combatable_methods = [x for x in dir(Combatable) if not x.startswith('_')]
    print(f"Combatable: {combatable_methods}")

    magical_methods = [x for x in dir(Magical) if not x.startswith('_')]
    print(f"Magical: {magical_methods}")

    elite_card = EliteCard(
        name="Arcane Warrior",
        cost=10,
        rarity="Legendary",
        attack=5,
        defense=3,
        health=10,
        mana=4
    )

    print(f"\nPlaying {elite_card.name} (Elite Card):")

    print("\nCombat phase:")
    attack_result = elite_card.attack("Enemy")
    print(f"Attack result: {attack_result}")

    defense_result = elite_card.defend(5)
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    spell_result = elite_card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    mana_result = elite_card.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
