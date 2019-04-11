from pygame import *
from random import randrange
from math import *
from Pong.PlayerRacket import PlayerRacket

class Ball:

    MAX_SPEED_Y =4

    def __init__(self,pos,rad,color,rigid):
        self.velocity = (Ball.MAX_SPEED_Y,randrange(-Ball.MAX_SPEED_Y,Ball.MAX_SPEED_Y))
        self.pos = pos
        self.color = color
        self.rad = rad
        self.rigid = rigid

    def update_move(self):
        # if there is collision
        self.pos = (self.velocity[0] + self.pos[0], self.pos[1] + self.velocity[1])
        self.collision_update()

    def draw(self,surface):
        self.update_move()
        draw.circle(surface,self.color,self.pos,self.rad)


    def collision_update(self):
        col_pos = (0,0)
        col_body = None
        collision = False
        for r in self.rigid:
            for point in ((self.pos[0] + self.rad*cos(theta*0.01),self.pos[1] + self.rad*sin(theta*0.01))   for theta in  range(0,int(pi*2*100))):
                if  r.posize[0] < point[0] < r.posize[0] + r.posize[2]  and r.posize[1] < point[1] < r.posize[1] + r.posize[3]:

                    col_pos = point
                    col_body = r
                    collision= True
                    break
        if collision and type(r) is PlayerRacket:
            self.velocity = (int(-self.velocity[0]),int((col_pos[1] - col_body.posize[1] +
                                                          col_body.posize[3]/2)/col_body.posize[3]*self.velocity[1]))



