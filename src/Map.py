class Map:
  def __init__(self, contamination):
    """
    columns = map columns, or number of columns
    rows = map rows, or number of rows
    contamination is a 2-D list of contamination values
    """
    self.rows = len(contamination) + 2
    self.columns = len(contamination[0]) + 2
    self.robots = []
    for i in range(self.rows):
      temp = []
      for j in range(self.columns):
        temp.append(0)
      self.robots.append(temp)
    # everything below this line surrounds the 2-D array with a border of 0's for the bases
    tempList = contamination
    tempList.insert(0, [0] * (self.columns - 2))
    tempList.append([0] * (self.columns - 2))
    for i in range(len(tempList)):
      l = tempList[i]
      l.insert(0, 0)
      l.append(0)
      tempList[i] = l 
    self.contamination = tempList
  
  def remove_robot(self, row, col):
    """

    removes a robot if it exists, at a certain location
    """
    self.robots[row][col] = 0
  
  def add_robot(self, row, col):
    """
    adds a robot at a certain location, it successful returns true, else returns false
    """
    if self.robots[row][col] != 0:
      return False
    else:
      self.robots[row][col] = 1

  def is_valid_square(self, row, col):
    """
    Determines whether or not a robot can be at a certain location
    """
    if (row == 0 or row == self.rows - 1) or (col == 0 or col == self.columns - 1):
      if self.contamination[row][col] != 'B':
        return False

    return True

  def add_base(self, coords):
    """
    Adds a base at the given coordinates
    """
    if (coords[1] != 0 and coords[1] != (self.columns - 1)) and (coords[0] != 0 and coords[0] != (self.rows - 1)):
      raise ValueError(f"Cannot place a base at {coords[0]}, {coords[1]}")
    self.contamination[coords[0]][coords[1]] = 'B'
    return None

  # def remaining_contamination(self):
  #   """
  #   Print the sum of all remaining contamination values
  #   """
  #   return sum([sum(i) for i in self.contamination])
  
  def remaining_tiles(self):
    """
    Print the coordinates of tiles which still need to be cleaned
    Returns a list a tuples (coordinates)
    """
    remaining = []
    for i in range(1, self.rows - 1):
      for j in range(1, self.columns - 1):
        if self.contamination[i][j] != 0:
          remaining.append((i, j)) # row, column
    return remaining
  
  def clean_tile(self, row, col, fluid_remaining):
    """
    Cleans the (row, col) tile.
    Takes fluid_remaining from the robot, and updates the contamination values accordingly
    Returns the amount of fluid used
    """
    if fluid_remaining == 0:
      return 0
    contam_value = self.contamination[row][col];
    if fluid_remaining >= contam_value:
      self.contamination[row][col] = 0
      return contam_value
    else:
      self.contamination[row][col] -= fluid_remaining
      return fluid_remaining

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
