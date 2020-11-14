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

    def find_next_move(map_array):
        i = pos_x
        j = pos_y
        
        #Loop through list of possible next locations
        # -plan of attack array
        #if no possible locations, go home

        #Find shortest distance location

        #if the dist is more than fuel
        #go back home

        


