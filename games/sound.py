# game with sound

import pygame
import sys
from pygame.locals import *
import time

pygame.init()

# setup display
DISPLAYSURF = pygame.display.set_mode((600, 927))
pygame.display.set_caption('HAL9000 sound')

# background
hal9000 = pygame.image.load('2001.jpg')

# sound
soundObj = pygame.mixer.Sound('just_what.wav')

# run game loop
while True:
    DISPLAYSURF.blit(hal9000, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    soundObj.play()
    time.sleep(3)
    soundObj.stop()
