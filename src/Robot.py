class Robot:
  def __init__(self, fuel_capacity, clean_capacity, position_x, position_y, base_x, base_y):
      self.fuel_cap = fuel_capacity
      self.clean_cap = clean_capacity
      self.pos_x = position_x
      self.pos_y = position_y
      self.base_x = base_x
      self.base_y = base_y



x = Robot(10, 15)

print(x.clean_cap)