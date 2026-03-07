def check_temperature(temp_str: str) -> int:
    try:
        try:
            value = int(temp_str)
        except ValueError:
            raise ValueError(f"{temp_str} is not a valid number.")
        if value > 40:
            raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C).")
        if value < 0:
            raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C).")
        print(f"Temperature {value}°C is perfect for plants!")
        return value
    except ValueError as e:
        print(f"Error: {e}")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    for test in ["25", "abc", "100", "-50"]:
        print(f"Testing temperature: {test}")
        check_temperature(test)
        print()
