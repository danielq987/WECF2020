from Map import Map
from Robot import Robot

def main():
    """
    Initialize Map and Robot from file input converted to ints
    """

    case1 = open("../test_cases/case1.txt")
    clean_capacity, fuel_capacity = [int(e) for e in case1.readline().split()]

    r = Robot(fuel_capacity, clean_capacity)

    rows, cols = [int(e) for e in case1.readline().split()]
    tile_rows = [case1.readline().split() for row in range(rows)]

    a = Map(rows, cols, tile_rows)

    print(a)

if __name__ == "__main__":
    main()
