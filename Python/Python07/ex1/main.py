from typing import Any
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    
    my_deck = Deck()
    
    # Create one of each card type
    lightning = SpellCard(name="Lightning Bolt", cost=3, rarity="Common", effect_type="damage")
    crystal = ArtifactCard(name="Mana Crystal", cost=2, rarity="Rare", durability=5, effect="+1 mana per turn")
    dragon = CreatureCard(name="Fire Dragon", cost=5, rarity="Legendary", attack=7, health=5)
    
    my_deck.add_card(lightning)
    my_deck.add_card(crystal)
    my_deck.add_card(dragon)
    
    print(f"Deck stats: {my_deck.get_deck_stats()}\n")
    print("Drawing and playing cards:\n")
    
    game_state: dict[str, Any] = {
        "player": {"mana": 10},
        "battlefield": []
    }
    
    while my_deck.cards:
        drawn_card = my_deck.draw_card()
        # Fallback to .type if .card_type isn't found (for backward compatibility with your ex0)
        card_type = getattr(drawn_card, "card_type", getattr(drawn_card, "type", "Unknown"))
        
        print(f"Drew: {drawn_card.name} ({card_type})")
        print(f"Play result: {drawn_card.play(game_state)}")
        
    print("\nPolymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()