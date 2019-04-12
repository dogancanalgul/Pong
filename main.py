import pygame, sys

from pygame.locals import *

#initializing pygame
from Pong.PlayerRacket import PlayerRacket
from Pong.Wall import Wall
from Pong.ball import Ball

pygame.init()

#Game Surface 480x480
HEIGHT = 640
WIDTH = 640
DisplaySurface = pygame.display.set_mode((WIDTH, HEIGHT))

#Game Name Pong
pygame.display.set_caption("Pong")

# pygame.draw.circle(DisplaySurface, (255, 255, 255), (int(WIDTH/2), int(HEIGHT/2)), 15)

rectangle = PlayerRacket((255, 255, 255), (0, 200, 20, 100), HEIGHT)
rect2 = PlayerRacket((255, 0, 255), (WIDTH - 20, 200, 20, 100), HEIGHT)


ball = Ball((int(WIDTH/2),int(HEIGHT/2)),10,(255,255,255),(rectangle,rect2
            #Adding upper and lower bounds to ball
           , Wall((0, -10, WIDTH, 10)) # TOP WALL
            , Wall((0, HEIGHT, WIDTH, 10))#BOTTOM WALL
))

#Game Loop
while True:

    #User Events;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #End Game
                pygame.quit()
                sys.exit()

    #KEYBOARD CONTROL
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        rectangle.moveUp()
        rect2.moveUp()
    elif keys[pygame.K_DOWN] :
        rectangle.moveDown()
        rect2.moveDown()



    #Update Display
    DisplaySurface.fill((0, 0, 0))

    rectangle.draw(DisplaySurface)
    rect2.draw(DisplaySurface)
    ball.draw(DisplaySurface)

    pygame.display.update()
    (pygame.time.Clock()).tick(60)



