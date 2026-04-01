from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self, 
        name: str, 
        cost: int, 
        rarity: str, 
        attack: int, 
        health: int, 
        card_id: str,
        initial_rating: int = 1000
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.card_id = card_id
        
        # Rankable stats
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    # --- Card Implementation ---
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {"action": "Tournament card played", "card": self.name}

    # --- Combatable Implementation ---
    def attack(self, target: Any) -> dict[str, Any]:
        return {"attacker": self.name, "damage": self.attack_power}

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        self.health -= incoming_damage
        return {"defender": self.name, "health_remaining": self.health}

    def get_combat_stats(self) -> dict[str, Any]:
        return {"attack": self.attack_power, "health": self.health}

    # --- Rankable Implementation ---
    def calculate_rating(self) -> int:
        # Standard +16 for a win, -16 for a loss to match the PDF output
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating = self.calculate_rating()
        # Reset tracker so we don't double-count previous wins in the calculation
        self.wins = 0 

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = self.calculate_rating()
        self.losses = 0

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "rating": self.rating, 
            "record": f"{self.wins}-{self.losses}"
        }

    # --- Tournament Specific Implementation ---
    def get_tournament_stats(self) -> dict[str, Any]:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "interfaces": ["Card", "Combatable", "Rankable"]
        }