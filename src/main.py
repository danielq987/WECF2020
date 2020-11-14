from Map import Map
from Robot import Robot
import json

def main():
    """
    Initialize Map and Robot from file input converted to ints
    """

    
    case1 = open("../test_cases/case1.txt")
    clean_capacity = case1.read()
    fuel_capacity = case1.read()

    r = Robot(fuel_capacity, clean_capacity)
    case1 = open("../test_cases/case1.txt")
    clean_capacity, fuel_capacity = [int(e) for e in case1.readline().split()]

    rows = case1.read()
    cols = case1.read()
    m = Map(rows, cols)
    r = Robot(fuel_capacity, clean_capacity)

    rows, cols = [int(e) for e in case1.readline().split()]
    tile_rows = [case1.readline().split() for row in range(rows)]

    m = Map(tile_rows)

    """
    MAIN LOOP STUFF
    """
    r1 = Robot(fuel_capacity, clean_capacity)
    r2 = Robot(fuel_capacity, clean_capacity)
    r3 = Robot(fuel_capacity, clean_capacity)
    r4 = Robot(fuel_capacity, clean_capacity)
    robot_array = [r1, r2, r3, r4]
    done = False    

    # MAIN LOOP
    while(not done):
        #Loop through each robot
        for r in robot_array:
            
            if(r.status != "complete"):
                if r.status == "none":
                    #find the nearest destination to clean up
                    #PLACEHOLDERS
                    next_x = 10
                    next_y = 10
                    no_contimated_spots_left = False

                    #check if no next, and current is base
                    if(no_contimated_spots_left):
                        if(r.pos_x == r.base_x and r.pos_y == r.base_y):
                            #Robot is done!
                            r.status = "complete"
                        else:
                            r.route_x = r.base_x
                            r.route_y = r.base_y
                            r.status = "to_base"
                    else:
                        # Set new route destination to this
                        r.route_x = next_x
                        r.route_y = next_y
                        
                        #Check what the next required move is
                        n_x, n_y = r.find_next_move()

                        #TODO: Make the next required move

                elif r.status == "to_base":
                    #Check what the next required move is
                    n_x, n_y = r.find_next_move()

                    # robot is at the destination of the route planned
                    if(n_x == 0 and n_y == 0):
                        # Refuel and acquire new fluid
                        r.fuel_cap = fuel_capacity
                        r.clean_cap = clean_capacity
                        r.status = "none"
            
                else:
                    #Check what the next required move is
                    n_x, n_y = r.find_move_vector()

                    # robot is at the destination of the route planned
                    # set status to clean as its next move
                    if(n_x == 0 and n_y == 0):
                        r.status = "clean"

                    # robot cannot reach the destination as it will run out of fuel
                    elif(n_x >= r.fuel_cap or n_y >= r.fuel_cap):
                        # set status to base as its next move
                        r.status = "to_base"
                        #TODO: make the first move towards base

                    #No issues encountered
                    else:
                        n_x, n_y = r.find_next_move()
                        r.x_pos += n_x
                        r.y_pos += n_y
            else:
                done = done and (r.status == "complete")











    final_output = json.dumps(m.history)

if __name__ == "__main__":
    main()
