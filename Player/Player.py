import pygame
from pygame import freetype

from Pong.Player.PlayerRacket import PlayerRacket


class Player:

    GAME_FONT:int


    def __init__(self, color, posize, limit,goal,pos):
        self.racket = PlayerRacket(color, posize, limit)
        self._score = 0
        self.goal = goal
        Player.GAME_FONT = freetype.Font("wonder.ttf", 24)
        self.pos = pos

    def update(self, surface):
        self.racket.draw(surface)
        text_surface,rect = Player.GAME_FONT.render(f"{self._score}", (255, 255, 255))
        surface.blit(text_surface,dest=self.pos)

    def up(self):
        self.racket.moveUp()

    def down(self):
        self.racket.moveDown()

    def score(self):
        self._score += 1

# A player Class and file to store all player related stuff. For starters
# I am going to take PlayerRacket to here and implement Goal. Then in Player Class
# I will make composition with them. After that I hope main will be much more clear for
# new tools such as menu screen, multiplayer and etc.
