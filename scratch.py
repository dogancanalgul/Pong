import pygame
import sys
from random import randint

display = True


class snakeGame:


    snake = [(16, 16),(16,15)]
    apple = (18, 18)
    is_dead = False
    is_left = False
    is_right = False

    def move_left(self):
        self.is_left = True
        self.move_forward()
        self.is_left = False
        self.is_right = False

    def move_right(self):
        self.is_right = True
        self.move_forward()
        self.is_left = False
        self.is_right = False


    def move_forward(self):

        vect = (self.snake[0][0] - self.snake[1][0], self.snake[0][1] - self.snake[1][1])
        if self.is_right:
            vect = (-vect[1], vect[0])
        elif self.is_left:
            vect = (vect[1], -vect[0])

        dest_pos = (self.snake[0][0] + vect[0],self.snake[0][1]+ vect[1])

        if not(0 <= dest_pos[0] < 32 and 0 <= dest_pos[1] < 32):
            self.is_dead =True

        elif dest_pos in self.snake:
            self.is_dead = True

        elif dest_pos == self.apple:
            prev_tail = self.snake[-1]

            for i in range(len(self.snake) - 1,0,-1):
                self.snake[i] = self.snake[i-1]
            self.snake[0] = dest_pos
            self.snake.append(prev_tail)

            #APPLE CREATION
            self.apple = (randint(0,32), randint(0,32))
            flag = True
            while flag:
                flag = False
                for pos in self.snake:
                    if pos[0] == self.apple[0] and pos[1] == self.apple[1]:
                        self.apple = (randint(0,32), randint(0,32))
                        flag = True
        else:
            for i in range(len(self.snake) - 1,0,-1):
                self.snake[i] = self.snake[i-1]
            self.snake[0] = dest_pos

    def game(self):

        if display:
            pygame.init()
            DisplaySurface = pygame.display.set_mode((640, 640))
            # Game Name Pong
            pygame.display.set_caption("Pong")

        self.is_dead = False
        while not self.is_dead:

            # User Events;
            if display:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                self.move_right()
            elif keys[pygame.K_LEFT]:
                self.move_left()
            
            self.move_forward()
            if display:
                DisplaySurface.fill((0,0,0))
                self.update(DisplaySurface)

            (pygame.time.Clock()).tick(16)

        pygame.quit()
        sys.exit()

    def update(self, surface):
        for elem in self.snake:
            pygame.draw.rect(surface, (255,255,255), (elem[0]*20,elem[1]*20,20,20))
        pygame.draw.rect(surface, (255, 0, 0), (self.apple[0] * 20,self.apple[1] * 20, 20, 20))


snakeGame().game()
