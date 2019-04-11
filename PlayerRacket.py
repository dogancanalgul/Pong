import pygame
from pygame.locals import *
class PlayerRacket:
    def __init__(self, color, posize, limit):
        self.color = color
        self.posize = posize
        self.POSLIMIT = limit

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.posize)
        return True

    def moveDown(self):
        tempList = list(self.posize)
        if tempList[1] + tempList[3] < self.POSLIMIT:
            tempList[1] += 1
        self.posize = tuple(tempList)

    def moveUp(self):
        print(self.posize)
        tempList = list(self.posize)
        if tempList[1] > 0:
            tempList[1] -= 1
        self.posize = tuple(tempList)

