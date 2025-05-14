import random
from threading import Timer
from unittest import skipIf


import pygame
from Common import *
import Common
from Player import Player
from Enemy import Enemy

# Подключаем pygame

# Создаем класс игрока





all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

bullets_sprites = pygame.sprite.Group()

enemy_sprites = pygame.sprite.Group()
enemy = Enemy(enemy_sprites)

while not Common.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Common.game_over = True
            timer.join()
            timer.join()
        exit()

    render()






# Создаем класс противника

# Инициализируем pygame
#pygame.init()

# Задаем ширину
#width = 1000
# Задаем высоту
#height = 500

# Создаем окно
#win = pygame.display.set_mode((width, height))

# Создаем переменную группы спрайтов
#all_sprites = pygame.sprite.Group()

# Создаем игрока
#player = Player(all_sprites)

# Создаем противника
#enemy_sprites = pygame.sprite.Group()
# Указываем ему позицию слева в 200 пикселей
#Enemy.rect.left = 200

# Добавляем игрока в группу спрайтов
#all_sprites.add(player)

# Создаем группу спрайтов противников
#enemy_sprites = pygame.sprite.Group()

# Добавляем противника в группу спрайтов противников
#enemy_sprites.add(Enemy)

#FPS = 60
#clock = pygame.time.Clock()
# Бесконечный игровой цикл
while True:
    # Перебираем все события
    for event in pygame.event.get():
        # Если произошло событие закрытия(нажали на крестик или ALT + F4)
        if event.type == pygame.QUIT:
            # Выходим из игры
            exit()

    # Определяем есть ли соприкосновение игрока с каким-либо спрайтом из группы спрайтов противников
    # Здесь player - сам игрок, enemy_sprites - группа спрайтов противников, True - нужно ли удалять спрайт при столкновении
    hits = pygame.sprite.spritecollide(player, enemy_sprites, True)
    # Заливаем задний фон белый цветом
    win.fill((255, 255, 255))
    # Рисуем все спрайты, который есть в группе
    all_sprites.draw()
    enemy_sprites.draw()
    bullets_sprites.draw()
    bullets_sprites.update()
    # Обновляем спрайты
    all_sprites.update()
    enemy_sprites.update()
    # Обновляем экран
    pygame.display.update()
    clock.tick(FPS)