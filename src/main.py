from Map import Map
from Robot import Robot
import json
import math

def get_number_of_bases(m, fuel_cap):
    """
    :param m: map object to be modified
    :param fuel_cap: max distance that can be traveled from the base
    :return: number of bases needed and adds bases to map object
    """
    rows = m.rows - 2
    cols = m.columns - 2
    bases_array = []

    area_of_effect = (fuel_cap // 2) * 2 - 1

    # if area of effect is large in comparison to the map
    if (area_of_effect // 2 + 1) >= min(rows, cols):
        count = 1
        flip = True
        # if cols > rows, flat
        if cols > rows:
            while count <= (cols + 1):
                if flip:
                    base = (0, count)
                    bases_array.append(base)
                    m.add_base(base)
                else:
                    base = (rows + 1, count)
                    bases_array.append(base)
                    m.add_base(base)
                flip = not flip
                count += (area_of_effect // 2 + 1)

        # if rows > cols, tall
        else:
            while count <= (rows + 1):
                if flip:
                    base = (count, 0)
                    bases_array.append(base)
                    m.add_base(base)
                else:
                    base = (count, cols + 1)
                    bases_array.append(base)
                    m.add_base(base)
                flip = not flip
                count += (area_of_effect // 2 + 1)

    # if the aoe is small in comparison to the map
    else:
        count = 1
        
        # add bases horizontally
        while True:
            try:
                base = (0, count)
                bases_array.append(base)
                m.add_base(base)
                base = (rows + 1, count + (area_of_effect // 4))
                bases_array.append(base)
                m.add_base(base)
                count += area_of_effect // 2
            except:
                break

        # add bases vertically
        count = area_of_effect // 2
        while count < (rows - area_of_effect // 2):
            base = (count, 0)
            bases_array.append(base)
            m.add_base(base)
            base = (cols + 1, count)
            bases_array.append(base)
            m.add_base(base)

    # rows_needed = rows // area_of_effect
    # cols_needed = cols // area_of_effect

    # row_spacing = math.ceil(rows / 2)
    # col_spacing = math.ceil(cols / 2)

    # if rows_needed != 0:
    #     row_spacing = math.ceil(rows / (rows_needed + 1))
    # if cols_needed != 0:
    #     col_spacing = math.ceil(cols / (cols_needed + 1))

    # for row in range(1, rows + 1, row_spacing * 2):
    #     m.add_base(row + row_spacing - 1, 0)
    #     bases_array.append((row + row_spacing - 1, 0))

    # number_of_bases = rows_needed + cols_needed + 1

    # cols_added = 0
    # if number_of_bases > 1:
    #     for col in range(1, cols + 1, col_spacing * 2):
    #         m.add_base(0, col + col_spacing - 1)
    #         bases_array.append((0, col + col_spacing - 1))
    #         cols_added += 1
    #     if cols_needed + 1 > cols_added:
    #         m.add_base(0, cols + 1)
    #         bases_array.append((0, col + col_spacing - 1))

    return bases_array


def main():
    """
    Converts file input to ints, and then intiliazes Map and Robots
    """

    case1 = open("C:/Github/WECF2020/test_cases/case5.txt")

    clean_capacity, fuel_capacity = [int(e) for e in case1.readline().split()]
    # r = Robot(fuel_capacity, clean_capacity)

    tile_rows = []
    case1.readline()
    while True:
        line = case1.readline()
        if len(line) == 0:
            break
        tile_rows.append([int(i) for i in line.split()])

    m = Map(tile_rows)

    bases = get_number_of_bases(m, fuel_capacity)
    

    """
    MAIN LOOP STUFF
    """
    robot_array = []
    
    # 65 corresponds to the ascii character A
    count = 65
    for i in bases:
        r = Robot(chr(count), fuel_capacity, clean_capacity, i[1], i[0], i[1], i[0], i[1], i[0], "none")
        robot_array.append(r)
        m.add_robot(i[0], i[1])
        count += 1

    done = False
    iteration = 0
    # MAIN LOOP
    while(not done):
        #Loop through each robot
        done = True
        for r in robot_array:
            
            if(r.status != "complete"):

                # when the robot has no assigned duty/status
                if r.status == "none":

                    # check if any contaminated (reachable) spots are left
                    is_contaminated_spots_left = r.is_contaminated_spots_left(m)
                    
                    #check if no next, and current is base
                    if (not is_contaminated_spots_left):
                        if(r.pos_x == r.base_x and r.pos_y == r.base_y):
                            #Robot is done!
                            r.status = "complete"
                        else:
                            r.route_x = r.base_x
                            r.route_y = r.base_y
                            r.status = "to_base"
                    else:
                        r.find_goal(m)
                        #TODO: execute move toward base routine
                        

                # when the robot has been assigned to go back to base (for whatever reason)
                elif r.status == "to_base":
                    #Check what the next required move is
                    n_x, n_y = r.find_next_move(m)

                    # robot is at the destination of the route planned
                    if(n_x == 0 and n_y == 0):
                        # Refuel and acquire new fluid
                        r.fuel_cap = fuel_capacity
                        r.clean_cap = clean_capacity
                        r.status = "none"
                        r.save_resupply()

                    else:
                        m.remove_robot(r.pos_y, r.pos_x)
                        r.pos_x += n_x
                        r.pos_y += n_y
                        m.add_robot(r.pos_y, r.pos_x)
                        r.fuel_cap -= 1
                        r.save_move()

                # when the robot has been assigned to go to a contamination site
                elif (r.status == "to_contamination"):
                    # find next move and move there
                    n_x, n_y = r.find_next_move(m)
                    if m.robots[r.pos_y + n_y][r.pos_x + n_x] != 0:
                        r.save_clean(0)
                        continue
                    m.remove_robot(r.pos_y, r.pos_x)
                    r.pos_x += n_x
                    r.pos_y += n_y
                    m.add_robot(r.pos_y, r.pos_x)
                    r.fuel_cap -= 1
                    r.save_move()
                    #Check what the next required move is
                    n_x, n_y = r.find_move_vector()

                    # robot is at the destination of the route planned
                    # set status to clean as its next move
                    if(n_x == 0 and n_y == 0):
                        r.status = "clean"

                        # > find amount to clean in map
                        clean_amount = m.clean_tile(r.pos_y, r.pos_x, r.clean_cap)
                        r.clean_cap -= clean_amount
                        r.save_clean(clean_amount)
                        # more fluid than needed to clean
                        if(r.clean_cap > 0):
                            # since cleaned, check for new assignment
                            r.status = "none"
                        # less than or equal amount of fluid needed to clean
                        else:
                            #Since fluid is empty, must return to base
                            r.status = "to_base" 

                done = False
            else:
                #check if robot is done and if past robots are also done
                done = done and (r.status == "complete")
        iteration += 1

    

    # output shit
    final_output = {}
    tempList = []
    for i in robot_array:
        tempList.append([i.name, [i.base_y - 1, i.base_x - 1]])
    final_output["robots"] = tempList

    tempList = []
    
    index = 0;
    count = 0;
    while True:
        for i in robot_array:
            try:
                tempList.append(i.history[index])
                count = 0
            except:
                count += 1
        if count > len(robot_array):
            break
        index += 1

    final_output["actions"] = tempList
    with open('output.json', 'w') as f:
        f.write(json.dumps(final_output))

    # dump final output
    #final_output = json.dumps(m.history)
    for i in robot_array:
        print(i.history)

if __name__ == "__main__":
    main()
