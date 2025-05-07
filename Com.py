from threading import Timer
import pygame

pygame.init()

width, height = 500, 500

win = pygame.display.set_mode((width, height))

FPS = 60
clock = pygame.time.Clock()


widthLevel1 = width / 2
heightLevel1 = height / 2
level1 = pygame.Surface((widthLevel1, heightLevel1))
level1.fill((0, 255, 0))


widthLevel2 = width / 2
heightLevel2 = height / 2
level2 = pygame.Surface((widthLevel2, heightLevel2))
level2.fill((255, 255, 0))

widthLevel3 = width / 2
heightLevel3 = height / 2
level3 = pygame.Surface((widthLevel3, heightLevel3))
level3.fill((255, 0, 0))

widthLevel4 = width / 2
heightLevel4 = height / 2
level4 = pygame.Surface((widthLevel4, heightLevel4))
level4.fill((0, 0, 0))

image = pygame.image.load('ded.png')
playerWidth = 50
playerHeight = 50
image = pygame.transform.scale(image, (playerWidth, playerHeight))

xPlayer = 0
yPlayer = 0

currentLevel = 1

font = pygame.font.Font(None, 30)# None - Название шрифта, 20 - размер

text = font.render("привет", True, (0, 0, 0))

level1Text = font.render("Уровень 1", True, (0, 0, 0))
level2Text = font.render("Уровень 2", True, (0, 0, 0))
level3Text = font.render("Уровень 3", True, (0, 0, 0))
level4Text = font.render("Уровень 4", True, (255, 255, 255))

timerText = font.render("00:00", True, (0, 0, 0))

timerSecond = 0
timerMinute = 0


def increaseTime():
    global timerSecond, timerMinute, game_over
    if timerSecond == 59:
        timerSecond = 0
        timerMinute += 1
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

level1Sound = pygame.mixer.Sound('1 уровень.mp3')
level2Sound = pygame.mixer.Sound('2 уровень.mp3')
level3Sound = pygame.mixer.Sound('3 уровень.mp3')
level4Sound = pygame.mixer.Sound('4 уровень.mp3')

l1SoundPlaying = False
l2SoundPlaying = False
l3SoundPlaying = False
l4SoundPlaying = False

level1Background = pygame.image.load('background1.png')
level1Background = pygame.transform.scale(level1Background, (widthLevel1, heightLevel1))
level2Background = pygame.image.load('background2.png')
level2Background = pygame.transform.scale(level2Background, (widthLevel2, heightLevel2))
level3Background = pygame.image.load('background3.png')
level3Background = pygame.transform.scale(level3Background, (widthLevel3, heightLevel3))
level4Background = pygame.image.load('background4.png')
level4Background = pygame.transform.scale(level4Background, (widthLevel4, heightLevel4))

def render():
    level1.blit(level1Background, (0, 0))
    level2.blit(level2Background, (0, 0))
    level3.blit(level3Background, (0, 0))
    level4.blit(level4Background, (0, 0))

    if timerSecond < 10:
        timerSecondStr = "0" + str(timerSecond)
    else:
        timerSecondStr = str(timerSecond)
    if timerMinute < 10:
        timerMinuteStr = "0" + str(timerMinute)
    else:
        timerMinuteStr = str(timerMinute)
    timerText = font.render(timerMinuteStr + ":" + timerSecondStr, True, (0, 0, 0))

    level1.blit(timerText, (widthLevel1 / 2 - timerText.get_width() / 2, 0))

    level1.blit(level1Text,
                (widthLevel1 / 2 - level1Text.get_width() / 2, heightLevel1 / 2 - level1Text.get_height() / 2))
    level2.blit(level2Text,
                (widthLevel1 / 2 - level2Text.get_width() / 2, heightLevel1 / 2 - level2Text.get_height() / 2))
    level3.blit(level3Text,
                (widthLevel1 / 2 - level3Text.get_width() / 2, heightLevel1 / 2 - level3Text.get_height() / 2))
    level4.blit(level4Text,
                (widthLevel1 / 2 - level4Text.get_width() / 2, heightLevel1 / 2 - level4Text.get_height() / 2))


def play_music():
    global l1SoundPlaying, l2SoundPlaying, l3SoundPlaying, l4SoundPlaying, currentLevel, level1Sound, level2Sound, level3Sound, level4Sound
    if currentLevel == 1:
        if not l1SoundPlaying:
            level2Sound.stop()
            level3Sound.stop()
            level4Sound.stop()
            level1Sound.play()
            l1SoundPlaying = True
            l2SoundPlaying = False
            l3SoundPlaying = False
            l4SoundPlaying = False
    elif currentLevel == 2:
        if not l2SoundPlaying:
            level1Sound.stop()
            level3Sound.stop()
            level4Sound.stop()
            level2Sound.play()
            l1SoundPlaying = False
            l2SoundPlaying = True
            l3SoundPlaying = False
            l4SoundPlaying = False
    elif currentLevel == 3:
        if not l3SoundPlaying:
            level1Sound.stop()
            level3Sound.play()
            level4Sound.stop()
            level2Sound.stop()
            l1SoundPlaying = False
            l2SoundPlaying = False
            l3SoundPlaying = True
            l4SoundPlaying = False
    elif currentLevel == 4:
        if not l4SoundPlaying:
            level1Sound.stop()
            level3Sound.stop()
            level4Sound.play()
            level2Sound.stop()
            l1SoundPlaying = False
            l2SoundPlaying = False
            l3SoundPlaying = False
            l4SoundPlaying = True
