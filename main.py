import pygame, sys

from Pong.GameStats import GameStats
from Pong.Player.Goal import Goal
from Pong.Player.Player import Player
from pygame import freetype
from Pong.ball import Ball



def start_game():

    if pygame.mouse.get_pressed()[0]:
        mousePos = pygame.mouse.get_pos()
        if GameStats.width // 2 + 125 > mousePos[0] > GameStats.width // 2 - 125 and \
                GameStats.height // 2 - 50 < mousePos[1] < GameStats.height // 2 + 50:
            GameStats.mod = "on_game"

    # Update Display
    DisplaySurface.fill((0, 0, 0))
    pygame.draw.rect(DisplaySurface, (255, 0, 0), (GameStats.width // 2 - 125, GameStats.height // 2 - 100, 250, 100))
    text_surface, rect = GameStats.FONT.render("Start Game", (255, 255, 255))
    DisplaySurface.blit(text_surface, dest=(GameStats.width // 2 - 118, GameStats.height // 2 - 60, 200, 100))


def on_game():
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


def end_game():
    pass


# initializing py-game
pygame.init()
GameStats.FONT = freetype.Font("wonder.ttf", 24)


DisplaySurface = pygame.display.set_mode((GameStats.width, GameStats.height))

# Game Name Pong
pygame.display.set_caption("Pong")

# GOALS ARE REVERSELY ADDED
player1 = Player((255, 255, 255), (0, 200, 20, 100),
                 Goal((GameStats.width, 0, 10, GameStats.height)), (GameStats.width/2-24, 0))

player2 = Player((255, 0, 255), (GameStats.width - 20, 200, 20, 100),
                 Goal((-10, 0, 10, GameStats.height)), (GameStats.width/2+24, 0))

ball = Ball((player1, player2))

# Game Loop
while True:

    # User Events;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # End Game
            pygame.quit()
            sys.exit()

    if GameStats.mod == "start_game":
        start_game()
    if GameStats.mod == "on_game":
        on_game()
    elif GameStats.mod == "game_over":
        end_game()

    pygame.display.update()
    (pygame.time.Clock()).tick(60)

# TODO
# Play Game Screen                      DONE
# Play 2 Local Player                   DONE
# Play versus Machine
# Play versus Artificial Intelligence
# Sounds
# Sound settings
