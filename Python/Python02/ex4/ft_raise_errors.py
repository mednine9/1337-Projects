def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(
                f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except Exception as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    s = check_plant_health("tomato", 5, 10)
    if s:
        print(s)
    print("\nTesting empty plant name...")
    s = check_plant_health("", 5, 10)
    if s:
        print(s)
    print("\nTesting bad water level...")
    s = check_plant_health("tomato", 15, 10)
    if s:
        print(s)
    print("\nTesting bad sunlight hours...")
    s = check_plant_health("tomato", 10, 0)
    if s:
        print(s)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    try:
        test_plant_checks()
    except Exception as e:
        print(f"Error: {e}")
