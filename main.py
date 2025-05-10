import Enemy
from threading import Timer
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Спасение Лунного Кота")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Игрок (Луник)
player_size = 50
player_x = 100
player_y = HEIGHT - player_size - 50
player_speed = 5
jump_height = 15
is_jumping = False
jump_count = jump_height

# Гравитация
gravity = 1

# Игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -jump_height:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = jump_height

    # Отрисовка игрока (пока просто квадрат)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()