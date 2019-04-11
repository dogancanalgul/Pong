from pygame import *
from random import randrange

class Ball:

    MAX_SPEED_Y = 2

    def __init__(self,pos,rad,color,tangibles):
        self.velocity = (2,randrange(1,Ball.MAX_SPEED_Y))
        self.pos = pos
        self.color = color
        self.rad = rad
        self.tangibles = tangibles

    def update_move(self):
        # if there is collision
        self.pos = (self.velocity[0] + self.pos[0], self.pos[1] + self.velocity[1])


    def draw(self,surface):
        self.update_move()
        draw.circle(surface,self.color,self.pos,self.rad)

    def collision(self):
        for t in self.tangibles:
            pass