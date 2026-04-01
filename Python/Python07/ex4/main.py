from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...")
    
    platform = TournamentPlatform()
    
    # Instantiate with the exact stats needed to mirror the PDF output
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, "dragon_001", 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 4, 3, "wizard_001", 1150)
    
    platform.register_card(dragon)
    platform.register_card(wizard)
    
    # Print Dragon initial stats
    d_stats = dragon.get_tournament_stats()
    print(f"{dragon.name} (ID: {dragon.card_id}):")
    print(f"Interfaces: [{', '.join(d_stats['interfaces'])}]")
    print(f"Rating: {dragon.rating}")
    print(f"Record: 0-0\n")
    
    # Print Wizard initial stats
    w_stats = wizard.get_tournament_stats()
    print(f"{wizard.name} (ID: {wizard.card_id}):")
    print(f"Interfaces: [{', '.join(w_stats['interfaces'])}]")
    print(f"Rating: {wizard.rating}")
    print(f"Record: 0-0\n")
    
    print("Creating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}\n")
    
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        print(f"{i}. {card.name}")
        print(f"   Rating: {card.rating} ({card.wins}-{card.losses})")
        
    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()