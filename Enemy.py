import random

import pygame

pygame.init()

# Враг (простой вариант)
enemy_size = 40
enemy_x = 500
enemy_y = HEIGHT - enemy_size - 50
enemy_speed = 2

# В игровом цикле:
enemy_x += enemy_speed
if enemy_x > WIDTH - enemy_size or enemy_x < 0:
    enemy_speed *= -1

pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, enemy_size, enemy_size))

# Проверка столкновения с врагом
enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
if player_rect.colliderect(enemy_rect):
    print("Game Over!")  # Можно добавить логику перезапуска