class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: int = 1) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def __str__(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return "(blooming)"

    def __str__(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} flowers {self.bloom()}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, prize_points: int):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} flowers {self.bloom()}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants = []


class GardenManager:
    _gardens = []

    @classmethod
    def create_garden_network(cls, gardens: list) -> None:
        cls._gardens += gardens
        print(f"Total gardens managed: {len(cls._gardens)}")

    @staticmethod
    def add_plant(garden: Garden, plant: Plant) -> None:
        garden.plants += [plant]
        print(f"Added {plant.name} to {garden.name}'s garden")

    @staticmethod
    def grow_all(garden: Garden) -> None:
        print(f"\n{garden.name} is helping all plants grow...")
        for plant in garden.plants:
            plant.grow()

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    class GardenStats:
        @staticmethod
        def analyze(garden: Garden) -> None:
            regular = 0
            flowering = 0
            prize = 0
            total_points = 0
            current_height = 0
            start_height = 0

            for plant in garden.plants:
                current_height += plant.height
                
                name = plant.__class__.__name__
                if name == "Plant":
                    regular += 1
                elif name == "FloweringPlant":
                    flowering += 1
                elif name == "PrizeFlower":
                    prize += 1
                    total_points += plant.prize_points

            total_growth = current_height - start_height
            score = current_height + (regular * 10) + (flowering * 10) + (prize * 10) + total_points

            print(f"Plants added: {len(garden.plants)}, Total growth: {total_growth}cm")
            print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
            return score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    
    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    oak = Plant("Oak Tree", 100, 20)
    rose = FloweringPlant("Rose", 25, 5, "red")
    sunflower = PrizeFlower("Sunflower", 50, 5, "yellow", 10)
    
    GardenManager.add_plant(alice_garden, oak)
    GardenManager.add_plant(alice_garden, rose)
    GardenManager.add_plant(alice_garden, sunflower)

    GardenManager.grow_all(alice_garden)

    print(f"\n=== {alice_garden.name}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice_garden.plants:
        print(plant)
    print("")

    narcissus = PrizeFlower("Narcissus", 60, 20, "White", 22)
    bob_garden.plants += [narcissus]

    # Run Stats
    alice_score = GardenManager.GardenStats.analyze(alice_garden)
    print(f"\nHeight validation test: {GardenManager.validate_height(100)}")
    
    bob_score = 60 + (1 * 10) + 22
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}") 
    
    GardenManager.create_garden_network([alice_garden, bob_garden])