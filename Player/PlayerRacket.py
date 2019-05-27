import pygame


class PlayerRacket:
    SPEED = 10

    def __init__(self, color, posize, limit, ):
        self.color = color
        self._posize = list(posize)
        self.POSLIMIT = limit

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self._posize)
        return True

    def moveDown(self):
        if self._posize[1] + self._posize[3] < self.POSLIMIT:
            self._posize[1] += PlayerRacket.SPEED

    def moveUp(self):
        if self._posize[1] > 0:
            self._posize[1] -= PlayerRacket.SPEED

    # With this two functions below you can call the rackets index from the class
    # Example racket_object[i] gives posize[i]

    def __getitem__(self, key):
        return self._posize[key]

    def __setitem__(self, key,key2):
        self._posize[key] = self._posize[key2]