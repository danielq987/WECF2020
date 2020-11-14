from Map import Map
from Robot import Robot
import json
import math

def get_number_of_bases(m, fuel_cap):
    rows = m.rows - 2
    cols = m.columns - 2

    area_of_effect = fuel_cap - 1

    rows_needed = rows // area_of_effect
    cols_needed = cols // area_of_effect

    row_spacing = math.ceil(rows / 2)
    col_spacing = math.ceil(cols / 2)

    if rows_needed != 0:
        row_spacing = math.ceil(rows / (rows_needed + 1))
    if cols_needed != 0:
        col_spacing = math.ceil(cols / (cols_needed + 1))

    for row in range(1, rows + 1, row_spacing * 2):
        m.add_base(row + row_spacing - 1, 0)

    number_of_bases = rows_needed + cols_needed + 1

    cols_added = 0
    if number_of_bases > 1:
        for col in range(1, cols + 1, col_spacing * 2):
            m.add_base(0, col + col_spacing - 1)
            cols_added += 1
        if cols_needed + 1 > cols_added:
            m.add_base(0, cols + 1)

    return number_of_bases


def main():
    """
    Converts file input to ints, and then intiliazes Map and Robots
    """

    case1 = open("../test_cases/case4.txt")

    clean_capacity, fuel_capacity = [int(e) for e in case1.readline().split()]
    # r = Robot(fuel_capacity, clean_capacity)

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
        done = True
        for r in robot_array:

            if(r.status != "complete"):

                # when the robot has no assigned duty/status
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
                        r.status = "to_contamination"
                        #TODO: execute move toward base routine
                        

                # when the robot has been assigned to go back to base (for whatever reason)
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
                        r.x_pos += n_x
                        r.y_pos += n_y
                        r.fuel_cap -= 1

                # when the robot has been assigned to go to a contamination site
                elif (r.status == "to_contamination"):
                    #Check what the next required move is
                    n_x, n_y = r.find_move_vector()

                    # robot is at the destination of the route planned
                    # set status to clean as its next move
                    if(n_x == 0 and n_y == 0):
                        r.status = "clean"
                        #TODO: execute cleaning routine
                        # > find amount to clean in map

                        amount_to_clean = 43 #PLACE HOLDER
                        # more fluid than needed to clean
                        if(r.clean_cap > amount_to_clean):
                            use_fluid(amount_to_clean)
                            #TODO: SUBTRACT AMOUNT FROM MAP
                            # since cleaned, check for new assignment
                            r.status = "none"
                        # less than or equal amount of fluid needed to clean
                        elif(r.clean_cap <= amount_to_clean):
                            use_fluid(r.clean_cap)
                            #TODO: SUBTRACT AMOUNT FROM MAP
                            #Since fluid is empty, must return to base
                            r.status = "to_base" 

                    # robot cannot reach the destination as it will run out of fuel
                    elif(n_x >= r.fuel_cap or n_y >= r.fuel_cap):
                        # set status to base as its next move
                        r.status = "to_base"
                        #TODO: execute move toward base routine

                    #No issues encountered
                    else:
                        #find the next move and move there
                        n_x, n_y = r.find_next_move()
                        r.x_pos += n_x
                        r.y_pos += n_y
                        r.fuel_cap -= 1
            else:
                #check if robot is done and if past robots are also done
                done = done and (r.status == "complete")



    # dump final output
    final_output = json.dumps(m.history)

if __name__ == "__main__":
    main()
