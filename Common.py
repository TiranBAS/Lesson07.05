import Common
from threading import Timer
import pygame

pygame.init()

width, height = 1000, 500

win = pygame.display.set_mode((width, height))

all_sprites = pygame.sprite.Group()

FPS = 60
clock = pygame.time.Clock()

background_image = pygame.image.load("gg.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

background_image2 = pygame.image.load("gg.jpg")
background_image2 = pygame.transform.scale(background_image2, (width, height))

background_X1 = 0
background_X2 = width

background_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.blit(background_image, (background_X1, 0))
    win.blit(background_image2, (background_X2, 0))
    background_X1 -= background_speed
    background_X2 -= background_speed
    if background_X2 == 0:
        background_X1 = width
    if background_X1 == 0:
        background_X2 = width
    all_sprites.draw(win)
    all_sprites.update()

    pygame.display.update()
    clock.tick(FPS)


def render():
    return None


def timer():
    return None