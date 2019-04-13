from pygame import *
from random import randrange
from math import *

from Pong.Player.GameStats import GameStats
from Pong.Player.PlayerRacket import PlayerRacket
from Pong.Wall import Wall


class Ball:

    MAX_SPEED_Y = 12
    SPEED_X = 6
    COLOR = (int(255), int(255), int(255))
    RADIUS: int = 10

    def __init__(self, rigid):
        self.velocity = (Ball.SPEED_X, randrange(-Ball.MAX_SPEED_Y,Ball.MAX_SPEED_Y))
        self.pos = (int(GameStats.width/2), int(GameStats.height/2))
        self.rigid = rigid

    def update_move(self):
        # if there is collision
        self.pos = (self.velocity[0] + self.pos[0], self.pos[1] + self.velocity[1])
        self.collision_update()
        if self.pos[0] < -5 or self.pos[0] > 640:
            self.pos = (320, 320)
            self.velocity = (Ball.SPEED_X, randrange(-Ball.MAX_SPEED_Y, Ball.MAX_SPEED_Y))

    def draw(self, surface):
        self.update_move()
        draw.circle(surface, Ball.COLOR, self.pos, Ball.RADIUS)

    def collision_update(self):
        col_pos = (0, 0)
        col_body = None
        collision = False
        for r in self.rigid:
            for point in ((self.pos[0] + Ball.RADIUS*cos(theta*0.01), self.pos[1] + Ball.RADIUS*sin(theta*0.01))
                          for theta in range(0, int(pi*2*100))):
                if r.posize[0] < point[0] < r.posize[0] + r.posize[2] and \
                        r.posize[1] < point[1] < r.posize[1] + r.posize[3]:
                    col_pos = point
                    col_body = r
                    collision = True
                    break
            if collision:
                break
        if collision:
            if type(r) is PlayerRacket:
                self.velocity = (-self.velocity[0], int((col_pos[1] - col_body.posize[1] -
                                                        col_body.posize[3]/2)/col_body.posize[3]*Ball.MAX_SPEED_Y*2))
                print("Racket hit")
            elif type(r) is Wall:
                self.velocity = (self.velocity[0], -self.velocity[1])
                print("Wall Hit")