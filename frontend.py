import pygame
from Snake import *
from Fruit import *

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
    return fruit.generate()

def grow_snake():
    return head.grow()

def get_next_move():
    return head.get_next_move()


pygame.init()
background = pygame.image.load("SnakeMap.png")
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Snake game")

run = True
next_move = [0, 0]
current_move = [0, 0]
i = 0
game_type = "SWAP"

MAP_GRID = []
for i in range(16):
    row = []
    for j in range(16):
        row.append('')
    MAP_GRID.append(row)

tail = SnakeBody([0,1], MAP_GRID, None)
body = SnakeBody([1,1], MAP_GRID, tail)
head = SwapSnake([2,1], MAP_GRID, body)

MAP_GRID[1][0] = tail
MAP_GRID[1][1] = body
MAP_GRID[1][2] = head
fruit = Fruit(MAP_GRID)
body.set_parent(head)
tail.set_parent(body)

while run:
    pygame.time.delay(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not run:
        break

    keys = pygame.key.get_pressed()
    screen.blit(background, (0, 0))

    if keys[pygame.K_w] and current_move != [0, 1]:
        next_move = [0, -1]
    elif keys[pygame.K_a] and current_move != [1, 0]:
        next_move = [-1, 0]
    elif keys[pygame.K_s] and current_move != [0, -1]:
        next_move = [0, 1]
    elif keys[pygame.K_d] and current_move != [-1, 0]:
        next_move = [1, 0]

    if i % 30 == 0:
        next_move_swap = generate_fruit()
        if next_move_swap and game_type == "SWAP":
            next_move = get_next_move()
        run = move_snake(next_move)
        current_move = next_move[:]
        if not run: break
    for row in get_map_grid():
        for snake_body in row:
            if str(type(snake_body)) == "<class 'Fruit.Fruit'>":
                pygame.draw.circle(screen, (0,0,255), (snake_body.get_y()*30 + 15, snake_body.get_x()*30 + 15), 15)
            elif snake_body:
                x = snake_body.get_position()[0]
                y = snake_body.get_position()[1]
                x_d = snake_body.get_direction()[0]
                y_d = snake_body.get_direction()[1]
                if next_move == [0, 0]:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x*30, y*30, 30, 30))
                else:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((x*30) + (x_d*(i%30)), (y*30) + (y_d*(i%30)), 30, 30))
    i+=1
    pygame.display.update()
pygame.quit()
