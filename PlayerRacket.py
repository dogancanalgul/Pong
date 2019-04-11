import pygame
from pygame.locals import *


class PlayerRacket:
    def __init__(self, color, posize, limit):
        self.color = color
        self.posize = list(posize)
        self.POSLIMIT = limit

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.posize)
        return True

    def moveDown(self):
        if self.posize[1] + self.posize[3] < self.POSLIMIT:
            self.posize[1] += 4

    def moveUp(self):
        if self.posize[1] > 0:
            self.posize[1] -= 4
