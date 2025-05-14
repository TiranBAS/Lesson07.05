from threading import Timer
import pygame


pygame.init()

width, height = 1000, 500

win = pygame.display.set_mode((width, height))

all_sprites = pygame.sprite.Group()

FPS = 60
clock = pygame.time.Clock()

player_size = 50
player_x = 100
player_y = height - player_size - 50
player_speed = 5
jump_height = 15
is_jumping = False
jump_count = jump_height

gravity = 1
clock = pygame.time.Clock()

image = pygame.image.load('player.jpg')
playerWidth = 40
playerHeight = 40
image = pygame.transform.scale(image, (playerWidth, playerHeight))
xPlayer = 0
yPlayer = 0
current = 1

font = pygame.font.Font(None, 30)# None - Название шрифта, 20 - размер



background_image = pygame.image.load("fon.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

background_image2 = pygame.image.load("fon.jpg")
background_image2 = pygame.transform.scale(background_image2, (width, height))

background_X1 = 0
background_X2 = width

background_speed = 5

text = font.render("привет", True, (0, 0, 0))

level1Text = font.render("t", True, (0, 0, 0))

timerText = font.render("00:00", True, (0, 0, 0))
timerSecond = 0
timerMinute = 0

def increaseTime():
    global timerSecond, timerMinute, game_over
    if timerSecond == 59:
        timerSecond == 0
        timerSecond += 1
    else:
        timerSecond += 1
        timer = Timer(1, increaseTime)
    if game_over:
        timer.join()
    else:
        timer.start()

timer = Timer(1, increaseTime)
timer.start()
game_over = False

will = pygame.mixer.Sound('449359103103a80.mp3')
moneySound = pygame.mixer.Sound('3d20874f20174bd.mp3')
SoundPlaying = False


def render():
    if timerSecond < 10:
        timerSecondStr = "0" + str(timerSecond)
    else:
        timerSecondStr = str(timerSecond)
    if timerMinute < 10:
        timerMinuteStr = "0" + str(timerMinute)
    else:
        timerMinuteStr = str(timerMinute)
        timerText = font.render(timerMinuteStr + ":" + timerSecondStr, True, (0, 0, 0))
    will.blit(timerText, (width / 2 - timerText.get_width() / 2, 0))


#def play_music():
    #if current == 1:





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
