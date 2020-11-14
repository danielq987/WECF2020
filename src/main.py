from Map import Map
from Robot import Robot

def main():
    case1 = open("../test_cases/case1.txt")  # open test cases and reads values
    clean_capacity = case1.read()
    fuel_capacity = case1.read()

    r = Robot(fuel_capacity, clean_capacity)  # initialize robot
    print(r)

    rows = case1.read()
    cols = case1.read()
    a = Map(rows, cols)  # initialize map
    print(Map)

if __name__ == "__main__":
    main()
