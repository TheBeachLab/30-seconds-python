# simple font

import pygame
import sys
from pygame.locals import *

pygame.init()

# setup display
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Text and fonts')

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# fonts
fontObj = pygame.font.Font('medusastory.otf', 100)  # font object
textObj = fontObj.render('Python Games!', True, BLACK)  # text object
textRectObj = textObj.get_rect()  # get the surrounding rectangle
textRectObj.center = (200, 150)  # set the center of the rectangle

# run game loop
while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
