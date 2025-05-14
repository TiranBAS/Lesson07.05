import pygame

pygame.init()

width, height = 500, 500

win = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('5370637397563401384.jpg')
        self.image = pygame.transform.scale(self.image, (100, 110))
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 5
        if keys[pygame.K_DOWN]:
            self.rect.top += 5
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.left += 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('ef2b7147d8831eb5fae2b1ca3c9804e7.jpg')
        self.image = pygame.transform.scale(self.image, (100, 110))
        self.rect = self.image.get_rect()
        self.rect.right = width
        self.health = 5


all_sprites = pygame.sprite.Group()

player = Player(all_sprites)

enemy_sprites = pygame.sprite.Group()

enemy = Enemy(enemy_sprites)

enemy2 = Enemy(enemy_sprites)
enemy2.rect.top = 200

FPS = 60
clock = pygame.time.Clock()

background_image = pygame.image.load("ec9d8d335442347d154a9d8f02fa04cf.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

background_image2 = pygame.image.load("ec9d8d335442347d154a9d8f02fa04cf.jpg")
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
    enemy_sprites.draw(win)
    enemy_sprites.update()
    '''for i in range(len(enemy_sprites_list)):
        if player.rect.right >= enemy_sprites_list[i].rect.left and \
            player.rect.left <= enemy_sprites_list[i].rect.right and \
            player.rect.bottom >= enemy_sprites_list[i].rect.top and \
            player.rect.top <= enemy_sprites_list[i].rect.bottom:
            print('Столкнулись')'''
    hits = pygame.sprite.spritecollide(player, enemy_sprites, False)
    print(hits)
    if len(hits) > 0:
        hits[0].health -= 1
        hits[0].rect.left = random.randint(0, width - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, height - hits[0].rect.height)
        if hits[0].health < 0:
            enemy_sprites.remove(hits[0])


    pygame.display.update()
    clock.tick(FPS)