import pygame

# Инициализация микшера
pygame.mixer.init()

# Загрузка файла музыки
pygame.mixer.music.load('3d20874f20174bd.mp3')  # укажите правильный путь к файлу

# Воспроизведение музыки
pygame.mixer.music.play(-1)  # -1 означает зацикливание

# Чтобы музыка играла, пока программа не завершится, добавьте задержку или цикл
import time
while pygame.mixer.music.get_busy():
    time.sleep(1)

# Когда нужно остановить музыку:
# pygame.mixer.music.stop()




import pygame

pygame.init()
pygame.mixer.init()

# Загрузка и запуск музыки
pygame.mixer.music.load('assets/your_music.mp3')
pygame.mixer.music.play(-1)  # зациклить музыку

# Основной цикл игры (пример)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Остановка музыки перед выходом
pygame.mixer.music.stop()
pygame.quit()