from Pong.Player import PlayerRacket
from Pong import GameStats
from pygame import freetype
from Pong.Player.Player import Player


class Bot(Player):

    def __init__(self, color, posize, goal, pos):
        super().__init__(color,posize,goal,pos)


    def update(self, surface):
        super().update(surface)

        if self.ball[1] < self.racket[1]:
            self.up()
        if self.ball[1] > self.racket[1]:
            self.down()

    def load_ball(self,ball):
        self.ball = ball
