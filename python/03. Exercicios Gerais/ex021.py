import pygame
from time import sleep

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)

pygame.quit()
