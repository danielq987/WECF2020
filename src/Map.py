class Map:
  def __init__(self, contamination):
    """
    columns = map columns, or number of columns
    rows = map rows, or number of rows
    contamination is a 2-D list of contamination values
    """
    self.rows = len(contamination) + 2
    self.columns = len(contamination[0]) + 2
    tempList = contamination
    tempList.insert(0, [0] * (self.columns - 2))
    tempList.append([0] * (self.columns - 2))
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
    if (col != 0 and col != (self.columns - 1)) and (row != 0 and row != (self.rows - 1)):
      raise ValueError(f"Cannot place a base at {row}, {col}")
    self.contamination[row][col] = 'B'
    return None

  def remaining_contamination(self):
    """
    Print the sum of all remaining contamination values
    """
    return sum([sum(i) for i in self.contamination])
  
  def remaining_tiles(self):
    """
    Print the coordinates of tiles which still need to be cleaned
    Returns a list a tuples (coordinates)
    """
    remaining = []
    for i in range(1, self.rows - 1):
      for j in range(1, self.columns - 1):
        if self.contamination[i][j] != 0:
          remaining.append((i, j))
    return remaining
  
  def clean_tile(self, row, col, fluid_remaining):
    """
    Cleans the (row, col) tile.
    Takes remaining robot_fluid and returns the robot fluid 
    """
    if fluid_remaining == 0:
      return None
    contam_value = self.contamination[row][col];
    if fluid_remaining >= contam_value:
      self.contamination[row][col] = 0
    else:
      self.contamination[row][col] -= fluid_remaining    


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
  contam = [[50, 55, 0], [1, 2, 3]]
  map1 = Map(contam)
  print(map1.rows)
  print(map1.columns)
  print(map1.remaining_contamination())
  map1.add_base(3, 3)
  print(map1.remaining_tiles())
  print(map1)
  
if __name__ == "__main__":
  main()
