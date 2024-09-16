
import pygame

pygame.init()

maze = [
 "YYYYYYYYYYYYYYYYYY",
"Y                Y",
"Y   Y   Y   YYYY Y",
"Y Y YYYYYY YY   Y Y",
"Y Y YYY YY Y YY  Y",
"Y Y        Y     Y",
"Y Y YYY YY YY    Y",
"Y Y YYY Y  Y YY  Y",
"Y       YYYY     Y",
"Y YY YY YYY  Y   Y",
"Y Y Y Y Y Y Y  Y Y",
"Y           Y    Y",
"Y Y YYY YYYYY    Y",
"Y Y YYY YYYY   Y Y",
"Y Y       Y  Y   Y",
"Y Y YYYYYYYYYYY  Y",
"Y Y    YEY   YYY Y",
"YYYYYYYY   Y     Y",
"YYYYYYYYYYYYYYYYYY",

]

max_row_len = max(len(row) for row in maze)
for i in range(len(maze)):
    maze[i] = maze[i].ljust(max_row_len, "Y")

title_size = 40
maze_width, maze_height = len(maze[0]), len(maze)
player_size = 30

screen_width, screen_height = maze_width * title_size, maze_height * title_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

player_x, player_y = 40, 40
player_speed = 5

def maze_game():

    global player_x, player_y

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and maze[player_y // title_size][(player_x - player_speed) // title_size] != "Y":
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and maze[player_y // title_size][(player_x + player_size + player_speed) // title_size] != "Y":
            player_x += player_speed
        if keys[pygame.K_UP] and maze[(player_y - player_speed) // title_size][player_x // title_size] != "Y":
            player_y -= player_speed
        if keys[pygame.K_DOWN] and maze[(player_y + player_size + player_speed) // title_size][player_x // title_size] != "Y":
            player_y += player_speed

        screen.fill(black)

        for y in range(maze_height):
            for x in range(maze_width):
                if maze[y][x] == "Y":
                    pygame.draw.rect(screen, white, pygame.Rect(x * title_size, y * title_size, title_size, title_size))
                elif maze[y][x] == "E":
                    pygame.draw.rect(screen, green, pygame.Rect(x * title_size, y * title_size, title_size, title_size))


        pygame.draw.rect(screen, red, pygame.Rect(player_x, player_y, player_size, player_size))

        if maze[player_y // title_size][player_x // title_size] == "E":
            print("Congrats Mate!!!")
            running = False
        pygame.display.update()

    pygame.quit()
    quit()
maze_game()
