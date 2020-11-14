from Map import Map

def manhattan_dist(pt1, pt2):
    return abs(pt2[1] - pt1[1]) + abs(pt2[0] - pt1[0])

class Robot:
    
    def __init__(self, name, fuel_capacity, clean_capacity, position_x=0, position_y=0, base_x=0, base_y=0, route_x=0, route_y=0, status="none"):
        self.name = name
        self.og_fuel_cap = fuel_capacity
        self.fuel_cap = fuel_capacity
        self.clean_cap = clean_capacity
        self.pos_x = base_x
        self.pos_y = position_y
        self.base_x = base_x
        self.base_y = base_y
        self.history = [[name, [base_x,base_y]]] # Holds history of moves
        self.route_x = route_x
        self.route_y = route_y
        self.status = status

    def set_base(self, row, col):
        self.base_x = col
        self.pos_x = col
        self.base_y = row
        self.pos_y = row
        
    def save_move(self):
        self.history.append([self.name, "move", [self.pos_x - 1,self.pos_y - 1]])

    def save_clean(self, fluid_used):
        self.history.append([self.name, "clean",fluid_used])

    def find_move_vector(self):
        """
        Using current coordinates and final coordinates, find the vector between them (x,y)
        """
        #Calculate the distance vector
        distx = self.route_x - self.pos_x
        disty = self.route_y - self.pos_y
        return (distx, disty)

    def find_next_move(self):
        """
        Using current coordinates and final coordinates, find the next move to make (x,y)
        """

        distx, disty = find_move_vector()
        #If moving in the x direction is still required
        if(distx != 0):
            mov_x = distx/abs(distx)
        #If moving in the y direction is still required
        elif(disty != 0):
            mov_y = disty/abs(disty)
        #If no more movement is required
        else:
            pass

        return (mov_x,mov_y)


    def find_goal(self, map_obj):
        """
        Updates route_x and route_y to the goal tile -> either the base or the closest uncleaned tile
        Returns True if its a tile
        Returns False if its not a tile  
        """
        remaining = map_obj.remaining_tiles() # remaining tiles
        minimum_dist = 999999
        print(remaining)

        # iterates over uncleaned tiles
        for i in remaining:
            dist_to_goal = manhattan_dist(i, (self.pos_y, self.pos_x))
            dist_goal_to_base = manhattan_dist(i, (self.base_y, self.base_x))
            if dist_to_goal < minimum_dist:
                if self.fuel_cap > dist_to_goal + dist_goal_to_base:
                    minimum_dist = dist_to_goal
                    # TODO - set status?
                    self.route_x = i[1]
                    self.route_y = i[0]
                    self.status = "to_contamination"

        if minimum_dist == 999999:
            self.status = "to_base"
            self.route_x = self.base_x
            self.route_y = self.base_y
            return False
        else:
            return True

    def is_contaminated_spots_left(self, map_obj):
        """ 
        Returns True if there are spots left
        """
        remaining = map_obj.remaining_tiles() # remaining tiles
        print(remaining)
        flag = False
        # iterates over uncleaned tiles
        for i in remaining:
            if manhattan_dist(i, (self.base_y, self.base_x)) <= self.og_fuel_cap // 2:
                flag = True
        return flag


    def use_fluid(self, fluid_to_use):
        """
        Save the fluid change amount used
        """
        self.clean_cap -= fluid_to_use
        self.save_clean(fluid_to_use)

    
    def __repr__(self):
        """
        Debugging
        """
        string = ""
        string += f"Name: {self.name}\n"
        string += f"Fluid Remaining: {self.clean_cap}\n"
        string += f"Fuel Remaining: {self.fuel_cap}\n"
        string += f"Status: {self.status}\n"
        string += f"Current Coords: ({self.pos_x}, {self.pos_y})\n"
        string += f"Goal Coords: ({self.route_x}, {self.route_y})\n"
        string += f"Base Coords: ({self.base_x}, {self.base_y})\n"
        return string

def main():
    contam = [[0, 5, 0], [1, 2, 3]]
    map1 = Map(contam)
    r1 = Robot("bob", 3, 300)
    r1.set_base(0, 2)
    map1.add_base(0, 2)
    r1.find_goal(map1)
    print(repr(r1))
    r1.find_goal(map1)
    print(map1)
    print(r1.no_contaminated_spots_left(map1))
if __name__ == "__main__":
  main()

        


