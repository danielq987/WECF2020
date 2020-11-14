class Map:
  def __init__(self, height, length, contamination):
    """
    length = map length, or number of columns
    height = map height, or number of rows
    contamination is a 2-D list of contamination values
    """
    self.height = height + 2
    self.length = length + 2
    tempList = contamination
    tempList.insert(0, [0] * length)
    tempList.append([0] * length)
    for i in range(len(tempList)):
      l = tempList[i]
      l.insert(0, 0)
      l.append(0)
      tempList[i] = l 
    self.contamination = tempList
  
  def add_base(self, row, col):
    """
    Adds a base at the given coordinates
    """
    if (col != 0 and col != (self.length - 1)) and (row != 0 and row != (self.height - 1)):
      raise ValueError(f"Cannot place a base at {row}, {col}")
    self.contamination[row][col] = 'B'
    return None

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
  map1.add_base(1,1)
  print(map1)
  
if __name__ == "__main__":
  main()
