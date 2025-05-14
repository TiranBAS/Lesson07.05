from Common import *
import Common


class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('player.jpg')
        self.image = pygame.transform.scale(self.image, (80, 50))
        self.rect = self.image.get_rect()

    def update(self):
        self.move_by_keys()

player_size = 50
player_x = 100
player_y = height - player_size - 50
player_speed = 5
jump_height = 15
is_jumping = False
jump_count = jump_height

gravity = 1
clock = pygame.time.Clock()
        # Если нажата стрелка вверх
        #if keys[pygame.K_UP]:
            # Двигаемся вверх   `1` *
            #self.rect.top -= 5
        # Если нажата стрелка влево
        #if keys[pygame.K_DOWN]:
            # Двигаемся вниз
            #self.rect.top += 5
            # Если нажата стрелка вниз
        #if keys[pygame.K_LEFT]:
            # Двигаемся влево
            #self.rect.left -= 5
            # Если нажата стрелка вправо
        #if keys[pygame.K_RIGHT]:
            # Двигаемся вправо
            #self.rect.left += 5
        #if keys[pygame.K_SPACE]:
            #is_jumping = True
        #else:
            #if jump_count >= - jump_height:
                #neg = 1
                #if jump_count < 0:
                    #neg = -1
                #player_y -= (jump_count ** 2) * 0.5 * neg
                #jump_count -= 1
            #else:
                #is_jumping = False
                #jump_count = jump_height



            #bullet = Bullet(bullets_sprites)
            #bullet.rect.bottom = self.rect.bottom
            #bullet.rect.centerx = self.rect.centerx

#class Bullet(pygame.sprite.Sprite):
    #def __init__(self, *group):
        #super().__init__(*group)
        #self.image = pygame.image.load('Enemy.png')
        #self.image = pygame.transform.scale(self.image, (40, 20))
        #self.rect = self.image.get_rect()

    #def update(self):
        #if self.rect.right < width:
            #self.rect.top += 5
        #else:
            #bullets_sprites.remove(self)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            timer.join()
            exit()

    render()

    #bullets_sprites = pygame.sprite.Group()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
