import random
from typing import Any
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only instances of Card can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
        total = len(self.cards)
        if total == 0:
            return {"error": "Empty deck"}

        creatures = sum(1 for c in self.cards if getattr(
            c, "card_type", "") == "Creature" or 
                        getattr(c, "type", "") == "Creature")
        spells = sum(1 for c in self.cards if getattr(
            c, "card_type", "") == "Spell")
        artifacts = sum(1 for c in self.cards if getattr(
            c, "card_type", "") == "Artifact")
        avg_cost = sum(c.cost for c in self.cards) / total

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
