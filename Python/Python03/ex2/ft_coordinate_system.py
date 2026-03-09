import sys
import math
from typing import Tuple


def calculate_distance(p1: Tuple[int, int, int], p2: Tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def parse_coordinates(coord_string: str) -> Tuple[int, int, int]:
    try:
        parts = coord_string.split(',')

        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])

        return (x, y, z)

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def main():
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)

    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}\n")

    valid_str = "3,4,0"
    print(f'Parsing coordinates: "{valid_str}"')
    parsed_pos = parse_coordinates(valid_str)
    if parsed_pos:
        print(f"Parsed position: {parsed_pos}")
        dist2 = calculate_distance(origin, parsed_pos)
        print(f"Distance between {origin} and {parsed_pos}: {dist2:.1f}\n")

    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    parse_coordinates(invalid_str)
    print()

    print("Unpacking demonstration:")
    x, y, z = parsed_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
