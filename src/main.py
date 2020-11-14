from Map import Map
from Robot import Robot
import json

def main():
    case1 = open("../test_cases/case1.txt")  # open test cases and reads values
    clean_capacity = case1.read()
    fuel_capacity = case1.read()
    """
    Initialize Map and Robot from file input converted to ints
    """

    r = Robot(fuel_capacity, clean_capacity)  # initialize robot
    print(r)
    case1 = open("../test_cases/case1.txt")
    clean_capacity, fuel_capacity = [int(e) for e in case1.readline().split()]

    rows = case1.read()
    cols = case1.read()
    a = Map(rows, cols)  # initialize map
    print(Map)
    r = Robot(fuel_capacity, clean_capacity)

    rows, cols = [int(e) for e in case1.readline().split()]
    tile_rows = [case1.readline().split() for row in range(rows)]

    a = Map(rows, cols, tile_rows)

    print(a)

    final_output = json.dumps(a.history)

if __name__ == "__main__":
    main()
