import pygame
import sys

pygame.init()

width, height = 800, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('kk')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

cell_size= 100

# Урaвни(1-стена, 2-бокс, 3-дверь, 4-перс)
levels = [
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 0, 3, 0, 3],
        [1, 0, 2, 2, 0, 0, 1],
        [1, 0, 0, 4, 0, 3, 1],
        [1, 0, 0, 0, 2, 0, 1],
        [1, 2, 0, 2, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
]

current_level = 0
player = None
boxes = []
key = []
walls = []


def Roon(level):
    global player, boxes, key, walls
    player = None
    boxes = []
    key = []
    walls = []

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 1:
                walls.append((x, y))
            elif level[y][x] == 2:
                boxes.append((x, y))
            elif level[y][x] == 3:
                key.append((x, y))
            elif level[y][x] == 4:
                player = [x, y]

    return level


level = Roon(levels[current_level])
clock = pygame.time.Clock()
running = True


def draw_game():
    screen.fill(white)

    for wall in walls:
        pygame.draw.rect(screen, black, (wall[0] * cell_size, wall[1] * cell_size, cell_size, cell_size))
    for target in key:
        pygame.draw.rect(screen, black, (target[0] * cell_size, target[1] * cell_size, cell_size, cell_size))
    for box in boxes:
        pygame.draw.rect(screen, black, (box[0] * cell_size, box[1] * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, red, (player[0] * cell_size, player[1] * cell_size, cell_size, cell_size))
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, black, (0, y), (width, y))

    pygame.display.update()


def check():
    for box in boxes:
        if box not in key:
            return False
    return True


def move_player(hx, hy):
    newX = player[0] + hx
    newY = player[1] + hy
    if (newX, newY) in walls:
        return

    if (newX, newY) in boxes:
        box_newX = newX + hx
        box_newY = newY + hy

        if (box_newX, box_newY) not in walls and (box_newX, box_newY) not in boxes:
            boxes.remove((newX, newY))
            boxes.append((box_newX, box_newY))
        else:
            return

    player[0] = newX
    player[1] = newY

    if check():
        global current_level
        current_level += 1
        if current_level < len(levels):
            Roon(levels[current_level])
        else:
            print("Поздравляем!")
            pygame.quit()
            sys.exit()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            if event.key == pygame.K_RIGHT:
                move_player(1, 0)

            if event.key == pygame.K_UP:
                move_player(0, -1)
            if event.key == pygame.K_DOWN:
                move_player(0, 1)
    draw_game()