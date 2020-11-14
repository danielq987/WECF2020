class Map:
  def __init__(self, height, length, contamination):
    """
    length = map length, or number of columns
    height = map height, or number of rows
    contamination is a 2-D list of contamination values
    """
    self.height = height 
    self.length = length
    self.contamination = contamination
  
  def remaining_contamination(self):
    """
    Print the sum of all remaining contamination values
    """
    return sum([sum(i) for i in self.contamination])
  
  def __str__(self):
    """
    Returns the 2-D array for printing purposes
    """
    string = ""
    for i in self.contamination:
      for j in i:
        string += str(j) + " "
      string += "\n"
    return string
  

def main():
  contam = [[50, 55, 100], [1, 2, 3]]
  map1 = Map(1, 2, contam)
  print(map1.remaining_contamination())
  print(map1)
  
if __name__ == "__main__":
  main()
