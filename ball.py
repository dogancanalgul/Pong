from pygame import *
from random import randrange
from math import *

from Pong.GameStats import GameStats
from Pong.Player.Goal import Goal
from Pong.Player.PlayerRacket import PlayerRacket


class Ball:

    MAX_SPEED_Y = 12
    SPEED_X = 6
    COLOR = (int(255), int(255), int(255))
    RADIUS: int = 10
    WIN_SCORE = 10

    def __init__(self, players):
        self.velocity = (Ball.SPEED_X, randrange(-Ball.MAX_SPEED_Y, Ball.MAX_SPEED_Y))
        self.pos = (int(GameStats.width/2), int(GameStats.height/2))
        self.players = players

    def update_move(self):
        # if there is collision
        self.pos = (self.velocity[0] + self.pos[0], self.pos[1] + self.velocity[1])
        self.collision_update()
        if self.pos[0] < -5 or self.pos[0] > 640:
            self.pos = (320, 320)
            self.velocity = (Ball.SPEED_X, randrange(-Ball.MAX_SPEED_Y, Ball.MAX_SPEED_Y))
        elif self.pos[1] < 0 or self.pos[1] > GameStats.height:
            self.velocity = (self.velocity[0], -self.velocity[1])

    def draw(self, surface):
        self.update_move()
        draw.circle(surface, Ball.COLOR, self.pos, Ball.RADIUS)

    def collision_update(self):
        col_pos = (0, 0)
        col_body = None
        collision = False

        for p in [self.players[0].racket, self.players[1].racket, self.players[0].goal, self.players[1].goal]:
            for point in ((self.pos[0] + Ball.RADIUS*cos(theta*0.01), self.pos[1] + Ball.RADIUS*sin(theta*0.01))
                          for theta in range(0, int(pi*2*100))):
                if p[0] < point[0] < p[0] + p[2] and \
                        p[1] < point[1] < p[1] + p[3]:
                    col_pos = point
                    col_body = p
                    collision = True
                    break
            if collision:
                break
        if collision:
            if type(col_body) is PlayerRacket:
                self.velocity = (-self.velocity[0], int((col_pos[1] - col_body[1] -
                                                        col_body[3]/2)/col_body[3]*Ball.MAX_SPEED_Y*2))
            elif type(col_body) is Goal:
                if self.players[0].goal == col_body:
                    if self.players[0].score() == self.WIN_SCORE:
                        self.players[0].reset()
                        self.players[1].reset()

                if self.players[1].goal == col_body:
                    if self.players[1].score() == self.WIN_SCORE:
                        self.players[0].reset()
                        self.players[1].reset()
                self.pos = (GameStats.width//2, GameStats.height//2)
                self.velocity = ((Ball.SPEED_X * ((-1) ** randrange(2))), randrange(-Ball.MAX_SPEED_Y, Ball.MAX_SPEED_Y))

    def __getitem__(self, key):
        return self.pos[key]

