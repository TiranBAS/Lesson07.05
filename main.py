import pygame
import sys
import time
from threading import Timer
pygame.init()

width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('kk')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255,0)
blue = (33, 33, 33)

cell_size= 100

# Урaвни(1-стена, 2-бокс, 3-дверь, 4-перс)
levels = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 4, 2, 0, 0, 2, 0, 0, 3],
        [1, 0, 0, 0, 2, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0, 2, 0, 1],
        [1, 0, 2, 0, 0, 2, 0, 0, 1],
        [3, 0, 0, 0, 2, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
]

current_level = 0
player = None
boxes = []
key = []
walls = []

pygame.mixer.init()

# Загрузка и запуск музыки
pygame.mixer.music.load('3d20874f20174bd.mp3')
pygame.mixer.music.play(-1)  # зациклить музыку

# Основной цикл игры (пример)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

time_left = 10  # 10 секунд
font = pygame.font.Font(None, 50)# None - Название шрифта, 20 - размер
timerText = font.render("00:00", True, (255, 0, 0))

timerSecond = 0
timerMinute = 0
running = True

def increaseTime():
    global timerSecond, timerMinute, running
    if not running:
        return
    if timerSecond == 59:
        timerSecond = 0
        timerMinute += 1
    else:
        timerSecond += 1
    timer = Timer(1, increaseTime)
    if running:
        timer.start()

timer = Timer(1, increaseTime)
timer.start()


def stop_timer():
    global running
    running = False


stop_thread = Timer(37, stop_timer)
stop_thread.start()


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
    screen.fill(black)

    for wall in walls:
        pygame.draw.rect(screen, blue, (wall[0] * cell_size, wall[1] * cell_size, cell_size, cell_size))
    for target in key:
        pygame.draw.rect(screen, red, (target[0] * cell_size, target[1] * cell_size, cell_size, cell_size))
    for box in boxes:
        pygame.draw.rect(screen, green, (box[0] * cell_size, box[1] * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, white, (player[0] * cell_size, player[1] * cell_size, cell_size, cell_size))

    for x in range(0, width, cell_size):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, black, (0, y), (width, y))

    if timerSecond < 10:
        timerSecondStr = "0" + str(timerSecond)
    else:
        timerSecondStr = str(timerSecond)
    if timerMinute < 10:
        timerMinuteStr = "0" + str(timerMinute)
    else:
        timerMinuteStr = str(timerMinute)
    timerText = font.render(timerMinuteStr + ":" + timerSecondStr, True, (255, 255, 255))

    screen.blit(timerText, (width / 2 - timerText.get_width() / 2, 0))
    pygame.display.update()

result = 0

def check():
    global result, current_level
    box_in_key = False
    for box in boxes:
        if box in key:
            box_in_key = True
            result += 1
            #levels[current_level][box[1]][box[0]] = 3
            boxes.remove(box)
            break

    return box_in_key


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
        global current_level, result, running
        current_level += 1
        if current_level < len(levels):
            Roon(levels[current_level])
        else:
            if result == 8: #box quantity
                print("Поздравляем!")
                running = False
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

pygame.mixer.music.stop()
pygame.quit()