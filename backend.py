from Snake import *
from Fruit import *

MAP_GRID = []
for i in range(16):
    row = []
    for j in range(16):
        row.append('')
    MAP_GRID.append(row)

HEAD_INITIAL_POSITION = [1, 2]
BODY_INITIAL_POSITION = [1, 1]

body = SnakeBody(BODY_INITIAL_POSITION, MAP_GRID, None)
head = SnakeHead(HEAD_INITIAL_POSITION, MAP_GRID, body)
fruit = Fruit(MAP_GRID)
body.set_parent(head)
MAP_GRID[2][1] = head
MAP_GRID[1][1] = body

def get_map_grid():
    return MAP_GRID

def get_map_str():
    map = ""
    for row in MAP_GRID:
        map+=str(row)+"\n"
    return map

def move_snake(direction):
    return head.move(direction)

def generate_fruit():
    fruit.generate()

def grow_snake():
    return body.grow()


