from typing import Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registered_cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.registered_cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        card1 = self.registered_cards.get(card1_id)
        card2 = self.registered_cards.get(card2_id)

        if not card1 or not card2:
            return {"error": "One or both cards not found"}

        self.matches_played += 1

        score1 = getattr(card1, 'attack_power', 0) + \
            getattr(card1, 'health', 0)
        score2 = getattr(card2, 'attack_power', 0) + \
            getattr(card2, 'health', 0)

        if score1 >= score2:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        # Process the results
        winner.update_wins(1)
        loser.update_losses(1)

        winner.wins += 1
        loser.losses += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list[TournamentCard]:
        return sorted(self.registered_cards.values(), key=lambda c: c.rating, reverse=True)

    def generate_tournament_report(self) -> dict[str, Any]:
        if not self.registered_cards:
            avg = 0
        else:
            total = sum(c.rating for c in self.registered_cards.values())
            avg = total // len(self.registered_cards)

        return {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
        }
