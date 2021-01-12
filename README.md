# WECF2020
WEC F2020 Solutions

The basics of the problem given for Waterloo Engineering Competition was that there exists a team of robots to clean a floor, with each tile having varying dirtiness values. The fuel capacity and cleaning capacity of the robots are given. Each robot must start at the edge of the floor, but the exact position on the edge can be freely determined.

The task was to write a program to ouput a json file including detailed instructions for each step, for each robot.

## Our solution:

To set up, we created classes for the floor and the robot, writing appropriate properties and methods. This problem involved two main parts: sectioning the floor based on the fuel efficiency of the robots, number of robots, and floor size; and finding the path for each robot.

### Sectioning the floor

Since the robots could only travel in cardinal directions, the maximum coverage area from the edge is in the shape of a right triangle. Depending on the size of this triangle relative to the floor size, different sectioning strategies will be needed.

//todo

### Pathfinding for each robot

//todo
