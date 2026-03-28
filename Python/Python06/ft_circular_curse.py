import alchemy.grimoire as grimoire

def main():
    print("=== Circular Curse Breaking ===")
    
    print("\nTesting ingredient validation:")
    print(f"validate_ingredients(\"fire air\"): {grimoire.validate_ingredients('fire air')}")
    print(f"validate_ingredients(\"dragon scales\"): {grimoire.validate_ingredients('dragon scales')}")
    
    print("\nTesting spell recording with validation:")
    print(f"record_spell(\"Fireball\", \"fire air\"): {grimoire.record_spell('Fireball', 'fire air')}")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {grimoire.record_spell('Dark Magic', 'shadow')}")
    
    print("\nTesting late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): {grimoire.record_spell('Lightning', 'air')}")
    
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")

if __name__ == "__main__":
    main()