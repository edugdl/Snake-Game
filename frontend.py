import pygame
import backend

pygame.init()
background = pygame.image.load("SnakeMap.png")
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Snake game")

run = True
next_move = [0, 0]
current_move = [0, 0]
i = 0

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
        run = backend.move_snake(next_move)
        backend.generate_fruit()
        current_move = next_move[:]
        if not run: break
    if next_move == [0, 0]:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(30, 30, 30, 30))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(30, 60, 30, 30))
    else:
        for row in backend.get_map_grid():
            for snake_body in row:
                if str(type(snake_body)) == "<class 'Fruit.Fruit'>":
                    pygame.draw.circle(screen, (0,0,255), (snake_body.get_y()*30 + 15, snake_body.get_x()*30 + 15), 15)
                elif snake_body:
                    x = snake_body.get_position()[0]
                    y = snake_body.get_position()[1]
                    x_d = snake_body.get_direction()[0]
                    y_d = snake_body.get_direction()[1]
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((x*30) + (x_d*(i%30)), (y*30) + (y_d*(i%30)), 30, 30))
        i+=1
    pygame.display.update()
pygame.quit()