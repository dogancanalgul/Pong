import pygame, sys

from Pong.GameStats import GameStats
from Pong.Player.Goal import Goal
from Pong.Player.Player import Player
from Pong.Wall import Wall
from Pong.ball import Ball

# initializing pygame
pygame.init()


DisplaySurface = pygame.display.set_mode((GameStats.width, GameStats.height))

# Game Name Pong
pygame.display.set_caption("Pong")
goal_1 = Goal((-10,0,10,GameStats.height))

goal_2 = Goal((GameStats.width,0,10,GameStats.height))

player1 = Player((255, 255, 255), (0, 200, 20, 100), GameStats.height,goal_2,(GameStats.width/2-24,0))
player2 = Player((255, 0, 255), (GameStats.width - 20, 200, 20, 100), GameStats.height,goal_1,(GameStats.width/2+24,0))

ball = Ball((player1, player2))

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
        player2.up()
    elif keys[pygame.K_DOWN]:
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