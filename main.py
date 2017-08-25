import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

rectImg = pygame.image.load('rect.png')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

rectx = 200
recty = 150

direction = 'right'
while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        rectx += 5
        if rectx == 280:
            direction = 'down'

    elif direction == 'down':
        recty += 5
        if recty == 220:
            direction = 'left'
    elif direction == 'left':
        rectx -= 5
        if rectx == 10:
            direction = 'up'
    elif direction == 'up':
        recty -= 5
        if recty == 10:
            direction = 'right'

    pygame.draw.rect(DISPLAYSURF, )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()
    fpsClock.tick(FPS)
