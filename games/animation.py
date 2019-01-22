# my first animated game

import pygame
import sys
from pygame.locals import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

# setup display
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

# define colors
WHITE = (255, 255, 255)

# character
charImg = pygame.image.load('cat.png')
catImg = charImg
catx = 10
caty = 10
direction = 'right'

# run main loop
while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catImg = pygame.transform.flip(charImg, True, False)
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        catImg = pygame.transform.flip(charImg, True, False)
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catImg = charImg
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        catImg = charImg
        caty -= 5
        if caty == 10:
            direction = 'right'
    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)      # set the max fps
