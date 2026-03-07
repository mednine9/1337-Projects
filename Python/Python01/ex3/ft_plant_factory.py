#!/usr/bin/python3
class Plant:
    created_plants = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.created_plants += 1

    def display_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def grow(self, amount: int = 1) -> None:
        self.height = self.height + amount

    def age(self, amount: int = 1) -> None:
        self.age = self.age + amount


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = (
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    )
    for p in plants:
        p.display_info()
    print(f"\nTotal plants created: {Plant.created_plants}")
