import random
from Common import *
import Common

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('Enemy.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, width - self.rect.width)
        self.rect.left = random.randint(0, height - self.rect.height)

#class Enemy(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    #def __init__(self, *group):
        # Вызываем конструктор самого класса Sprite
        #super().__init__(*group)
        # Загружаем изображение
        #self.image = pygame.image.load('Enemy.png')
        # Настраиваем его. Не нужно здесь ничего менять, просто копируйте
        #self.image = self.image.convert()
        #colorkey = self.image.get_at((0, 0))
        #self.image.set_colorkey(colorkey)
        # Задаем размер(ЕСЛИ НУЖНО. ЕСЛИ НЕ НУЖНО - НЕ ПИШИТЕ ЭТУ СТРОКУ). Первая 100 - ширина картинки, вторая 100 - высота картинки
        #self.image = pygame.transform.scale(self.image, (100, 100))
        # Задаем границы описывающего прямоугольника
        #self.rect = self.image.get_rect()

# Враг (простой вариант)
#enemy_size = 40
#enemy_x = 500
#enemy_y = HEIGHT - enemy_size - 50
#enemy_speed = 2

# В игровом цикле:
#enemy_x += enemy_speed
#if enemy_x > WIDTH - enemy_size or enemy_x < 0:
    #enemy_speed *= -1

#pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, enemy_size, enemy_size))

# Проверка столкновения с врагом
#enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
#if player_rect.colliderect(enemy_rect):
    #print("Game Over!")  # Можно добавить логику перезапуска