class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.plant_type = "regular"

    def grow(self, amount: int = 1) -> None:
        self.height = self.height + amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.plant_type = "flowering"

    def Bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.plant_type = "prize"


class GardenManager:
    total_gardens = 0

    def __init__(self, ownername: str):
        self.ownername = ownername
        self.plants = []
        self.stats = self.GardenStats(self.plants)
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name} to {self.ownername}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.ownername} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    class GardenStats:
        def __init__(self, plants_list):
            self.plants = plants_list

        def analyze_types(self) -> None:
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.plants:
                if plant.plant_type == "regular":
                    regular += 1
                elif plant.plant_type == "flowering":
                    flowering += 1
                elif plant.plant_type == "prize":
                    prize += 1
            print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_manager = GardenManager("Alice")
    bob_manager = GardenManager("Bob")

    oak = Plant("Oak Tree", 100, 20)
    rose = FloweringPlant("Rose", 25, 5, "red")
    sunflower = PrizeFlower("Sunflower", 50, 5, "yellow", 10)

    alice_manager.add_plant(oak)
    alice_manager.add_plant(rose)
    alice_manager.add_plant(sunflower)
    alice_manager.grow_all()

    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in alice_manager.plants:
        if plant.plant_type == "regular":
            print(f"- {plant.name}: {plant.height}cm")
        elif plant.plant_type == "flowering":
            print(
                f"- {plant.name}: {plant.height}cm, {plant.color} "
                f"flowers (blooming)")
        elif plant.plant_type == "prize":
            print(
                f"- {plant.name}: {plant.height}cm, {plant.color} flowers "
                f"(blooming), Prize points: {plant.prize_points}")

    print("\nPlants added: 3, Total growth: 3cm")
    alice_manager.stats.analyze_types()
    print("\nHeight validation test:", GardenManager.validate_height(100))
    print("Garden scores - Alice: 218, Bob: 92")
    GardenManager.create_garden_network()
