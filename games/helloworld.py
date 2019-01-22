# My first game

import pygame
import sys
# to use pygame.locals functions as built-in. See [1]
from pygame.locals import *

pygame.init()

# setup window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('My first Python Game!')

# setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0),
                                         (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, RED, (60, 60), (500, 400), 2)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 100), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, WHITE, (200, 100, 100, 40))
pygame.draw.rect(DISPLAYSURF, BLACK, (10, 20, 100, 200))

pixels = pygame.PixelArray(DISPLAYSURF)
pixels[480][320] = BLACK
pixels[300, 300] = RED
del pixels


# run the game loop
while True:  # run this forever
    for event in pygame.event.get():
        if event.type == QUIT:  # [1] instead of pygame.locals.QUIT
            pygame.quit()
            sys.exit()
    pygame.display.update()
