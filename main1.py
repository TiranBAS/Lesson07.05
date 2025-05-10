# Подключаем pygame
from threading import Timer
import pygame
import pygame
from Common import *
import Common

# Создаем класс игрока
class Player(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    def __init__(self):
        # Вызываем конструктор самого класса Sprite
        super().__init__()
        # Загружаем изображение
        self.image = pygame.image.load('smile.png')
        # Настраиваем его. Не нужно здесь ничего менять, просто копируйте
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        # Задаем размер(ЕСЛИ НУЖНО. ЕСЛИ НЕ НУЖНО - НЕ ПИШИТЕ ЭТУ СТРОКУ). Первая 100 - ширина картинки, вторая 100 - высота картинки
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Задаем границы описывающего прямоугольника
        self.rect = self.image.get_rect()

    # Функция, которая определяет что будет происходить с игроком при обновлении экрана
    def update(self):
        # Определяем какие клавиши клавиатуры были нажаты
        keys = pygame.key.get_pressed()
        # Если нажата стрелка вверх
        if keys[pygame.K_UP]:
            # Двигаемся вверх   `1` *
            self.rect.top -= 5
        # Если нажата стрелка влево
        if keys[pygame.K_DOWN]:
            # Двигаемся вниз
            self.rect.top += 5
        # Если нажата стрелка вниз
        if keys[pygame.K_LEFT]:
            # Двигаемся влево
            self.rect.left -= 5
        # Если нажата стрелка вправо
        if keys[pygame.K_RIGHT]:
            # Двигаемся вправо
            self.rect.left += 5

# Создаем класс противника
class Enemy(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    def __init__(self):
        # Вызываем конструктор самого класса Sprite
        super().__init__()
        # Загружаем изображение
        self.image = pygame.image.load('smile2.png')
        # Настраиваем его. Не нужно здесь ничего менять, просто копируйте
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        # Задаем размер(ЕСЛИ НУЖНО. ЕСЛИ НЕ НУЖНО - НЕ ПИШИТЕ ЭТУ СТРОКУ). Первая 100 - ширина картинки, вторая 100 - высота картинки
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Задаем границы описывающего прямоугольника
        self.rect = self.image.get_rect()

# Инициализируем pygame
pygame.init()

# Задаем ширину
width = 500
# Задаем высоту
height = 500

# Создаем окно
win = pygame.display.set_mode((width, height))

# Создаем переменную группы спрайтов
all_sprites = pygame.sprite.Group()

# Создаем игрока
player = Player()

# Создаем противника
enemy = Enemy()
# Указываем ему позицию слева в 200 пикселей
enemy.rect.left = 200

# Добавляем игрока в группу спрайтов
all_sprites.add(player)

# Создаем группу спрайтов противников
enemy_sprites = pygame.sprite.Group()

# Добавляем противника в группу спрайтов противников
enemy_sprites.add(enemy)

FPS = 60
clock = pygame.time.Clock()
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
    all_sprites.draw(win)
    enemy_sprites.draw(win)

    # Обновляем спрайты
    all_sprites.update()
    enemy_sprites.update()
    # Обновляем экран
    pygame.display.update()
    clock.tick(FPS)