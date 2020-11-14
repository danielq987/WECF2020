from Map import Map
from Robot import Robot

def main():
  case1 = open("../test_cases/case1.txt")
  clean_capacity = case1.read()
  fuel_capacity = case1.read()

  r = Robot(fuel_capacity, clean_capacity)
  print(r)

  a = Map(1, 2)
  print(Map)
  
if __name__ == "__main__":
  main()
