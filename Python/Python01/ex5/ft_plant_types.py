class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int, shade: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.shade} "
              "square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str,  nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self. nutritional_value = nutritional_value


if __name__ == "__main__":
    flowers = (
      Flower("Rose", 25, 30, "red"),
      Flower("Sunflower", 150, 45, "yellow")
    )
    trees = (
      Tree("Oak", 500, 1825, 50, 78),
      Tree("Pine", 800, 3650, 40, 50)
    )
    vegitables = (        
    Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
    Vegetable("Carrot", 20, 60, "autumn", "vitamin A")
    )
    print("=== Garden Plant Types ===")
    for flower in flowers:
      print()
      print(f"{flower.name} (Flower): {flower.height}cm, "
            f"{flower.age} days, {flower.color} color")
      flower.bloom()
    for tree in trees:
      print()
      print(f"{tree.name} (Tree): {tree.height}cm, "
            f"{tree.age} days, {tree.trunk_diameter}cm diameter")
      tree.produce_shade()
    for vegitable in vegitables:
      print()
      print(f"{vegitable.name} (Vegetable): {vegitable.height}cm, "
            f"{vegitable.age} days, {vegitable.harvest_season} harvest")
      print(f"{vegitable.name} is rich in {vegitable.nutritional_value}")

    
