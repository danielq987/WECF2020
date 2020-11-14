from Map import Map
from Robot import Robot
import json

def main():
    """
    Initialize Map and Robot from file input converted to ints
    """
    case1 = open("../test_cases/case1.txt")
    clean_capacity = case1.read()
    fuel_capacity = case1.read()

    r = Robot(fuel_capacity, clean_capacity)
    case1 = open("../test_cases/case1.txt")
    clean_capacity, fuel_capacity = [int(e) for e in case1.readline().split()]

    rows = case1.read()
    cols = case1.read()
    m = Map(rows, cols)
    r = Robot(fuel_capacity, clean_capacity)

    rows, cols = [int(e) for e in case1.readline().split()]
    tile_rows = [case1.readline().split() for row in range(rows)]

    m = Map(tile_rows)

    final_output = json.dumps(m.history)

if __name__ == "__main__":
    main()
