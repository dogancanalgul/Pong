from Pong.Player import Player
from Pong.Player import PlayerRacket
from Pong import GameStats
from pygame import freetype

class Bot(Player):

    def __init__(self, color, posize, goal, pos):
        self._racket = PlayerRacket(color, posize, GameStats.height)
        self._score = 0
        self._goal = goal
        Player.GAME_FONT = freetype.Font("wonder.ttf", 24)
        self._score_pos = pos

    def update(self):
        super().update()

        if self.ball[1] > self._racket[1] :
            self.up()

        else :
            self.down()

