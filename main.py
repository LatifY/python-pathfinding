from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from pyfiglet import figlet_format as ff

import time as t

#finder
finder = AStarFinder(diagonal_movement=DiagonalMovement.always)


print(ff("Path Finder")+"\n")
print("0 = Obstacle")
print("1 = Way\n")

is_error = False

def error(msg):
    is_error = True
    print("*"*20)
    print(msg)
    print("*"*20+"\n")
    t.sleep(2)

while True:
    is_error = False
    w = int(input("Matrix Width: "))
    h = int(input("Matrix Height: "))
    if(h <= 0 or w <= 0): 
        error("Invalid Matrix Size!")
        continue
    
    print(f"Type a matrix({w}-{h})")

    matrix = []
    for y in range(h):
        if(is_error):continue
        sub_matrix = []
        horizontal = str(input())
        for i in horizontal.split(" "):
            if(is_error):continue
            num = int(i)
            if(num != 1 and num != 0):
                error(f"Invalid Input Numbers - ({num}?)")
                is_error = True
                continue
            sub_matrix.append(num)
        if(len(sub_matrix) != w and is_error == False):
            error("Invalid Width!")
            is_error=True
            continue
        matrix.append(sub_matrix)
    
    if(error):continue
    grid = Grid(matrix=matrix)

    sx, se = map(int,input("Start Position: ").split())
    ex, ee = map(int,input("End Position: ").split())


    start = grid.node(sx,se)
    end = grid.node(ex,ee)

    path, runs = finder.find_path(start,end,grid)

    print("\nPath Length: ", len(path))
    print("*"*20)
    for way in path:
        print(way)
    print("*"*20)
    print("Operations: ", runs)
    print(grid.grid_str(path=path,start=start, end=end))

    print("\n")
    again = str(input("Again(y/n): "))
    if(again.lower() == "y"): 
        print("\n")
        continue
    else:
        print("sea ya ;)")
        break