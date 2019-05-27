import pygame
from pygame import freetype
from Pong.GameStats import GameStats
from Pong.Player.PlayerRacket import PlayerRacket


class Player:

    GAME_FONT:int



    def __init__(self, color, posize, limit,goal,pos):
        self._racket = PlayerRacket(color, posize, limit)
        self._score = 0
        self._goal = goal
        Player.GAME_FONT = freetype.Font("wonder.ttf", 24)
        self._score_pos = pos

    # For getting the _goal and _racket attribute (they cannot be changed)

    @property
    def goal(self):
        return self._goal

    @property
    def racket(self):
        return self._racket

    def update(self, surface):
        self._racket.draw(surface)
        text_surface,rect = Player.GAME_FONT.render(f"{self._score}", (255, 255, 255))
        surface.blit(text_surface,dest=self._score_pos)

    def up(self):
        self._racket.moveUp()

    def down(self):
        self._racket.moveDown()

    def score(self):
        self._score += 1
        return self._score

    def reset(self):
        self._score = 0
        self.racket._posize[1] = GameStats.height//2

# A player Class and file to store all player related stuff. For starters
# I am going to take PlayerRacket to here and implement Goal. Then in Player Class
# I will make composition with them. After that I hope main will be much more clear for
# new tools such as menu screen, multi-player and etc.
