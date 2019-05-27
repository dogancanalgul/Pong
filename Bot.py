from Pong.Player import PlayerRacket
from Pong import GameStats
from pygame import freetype
from Pong.Player import Player

class Bot(Player):

    def __init__(self, color, posize, goal, pos):
        super().__init__(self,color,posize,goal,pos)


    def update(self):
        super().update()

        if self.ball[1] > self._racket[1] :
            self.up()

        else :
            self.down()

    def load_ball(self,ball):
        self.ball = ball