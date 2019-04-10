import pygame, sys

from pygame.locals import *

#initializing pygame

pygame.init()


#Game Surface 480x480
HEIGHT = 480
WIDTH = 480
DisplaySurface = pygame.display.set_mode((WIDTH, HEIGHT))

#Game Name Pong
pygame.display.set_caption("Pong")

pygame.draw.rect(DisplaySurface, (255, 255, 255), (0, 240, 20, 80))
pygame.draw.rect(DisplaySurface, (255, 255, 255), (180, HEIGHT - 20, 20, 80))
pygame.draw.circle(DisplaySurface, (255, 255, 255), (int(WIDTH/2), int(HEIGHT/2)), 120)

#Game Loop
while True:

    #User Events;
    for event in pygame.event.get():
        if event.type == QUIT:
            #End Game
                pygame.quit()
                sys.exit()
    #Update Display
    pygame.display.update()