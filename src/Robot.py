class Robot:
    
    def __init__(self, name, fuel_capacity, clean_capacity, position_x, position_y, base_x, base_y, route_x, route_y, on_route):
        self.fuel_cap = fuel_capacity
        self.clean_cap = clean_capacity
        self.pos_x = position_x
        self.pos_y = position_y
        self.base_x = base_x
        self.base_y = base_y
        self.on_route = on_route
        self.history = [[name, [base_x,base_y]]] # Holds history of moves
        self.route_x = route_x
        self.route_y = route_y

        
    def save_move(self, move_x, move_y):
        self.history.append([self.name, "move", [move_x,move_y]])

    def save_clean(self, fluid_used):
        self.history.append([self.name, "clean",fluid_used])
        pass

    def find_next_move(self):
        """
        Using current coordinates and final coordinates, find the next move to make (x,y), and save move
        """

        #Calculate the distance vector
        distx = self.route_x - self.pos_x
        disty = self.route_y - self.pos_y
        mov_x = 0
        mov_y = 0
        #If moving in the x direction is still required
        if(distx != 0):
            mov_x = distx/abs(distx)
        #If moving in the y direction is still required
        elif(disty != 0):
            mov_y = disty/abs(disty)
        #If no more movement is required
        else:
            pass

        #Save move to history and return move
        self.save_move(mov_x,mov_y)
        return (mov_x,mov_y)

    def use_fluid(self, fluid_to_use):
        """
        Save the fluid change amount used
        """
        self.fuel_cap -= fluid_to_use
        self.save_clean(fluid_to_use)




        
        #Loop through list of possible next locations
        # -plan of attack array
        #if no possible locations, go home

        #Find shortest distance location

        #if the dist is more than fuel
        #go back home

        


