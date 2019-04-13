import pygame, sys

from Pong.Player.GameStats import GameStats
from Pong.Player.Player import Player
from Pong.Wall import Wall
from Pong.ball import Ball

# initializing pygame
pygame.init()

DisplaySurface = pygame.display.set_mode((GameStats.width, GameStats.height))

# Game Name Pong
pygame.display.set_caption("Pong")


player1 = Player((255, 255, 255), (0, 200, 20, 100), GameStats.height)
player2 = Player((255, 0, 255), (GameStats.width - 20, 200, 20, 100), GameStats.height)

ball = Ball((player1.racket, player2.racket
            # Adding upper and lower bounds to ball
           , Wall((0, -10, GameStats.width, 10)) # TOP WALL
            , Wall((0, GameStats.height, GameStats.width, 10))#BOTTOM WALL
))

# Game Loop
while True:

    # User Events;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # End Game
                pygame.quit()
                sys.exit()

    # KEYBOARD CONTROL
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        # player1.up()
        player2.up()
    elif keys[pygame.K_DOWN]:
        # player1.down()
        player2.down()

    if keys[pygame.K_w]:
        player1.up()
    elif keys[pygame.K_s]:
        player1.down()


    # Update Display
    DisplaySurface.fill((0, 0, 0))

    player1.update(DisplaySurface)
    player2.update(DisplaySurface)
    ball.draw(DisplaySurface)

    pygame.display.update()
    (pygame.time.Clock()).tick(60)