# import pygame
# from pygame.locals import* 
# import time

# class Snake:
#     def __init__(self,parent_screen):
#         self.parent_screen=parent_screen
#         self.block_x=100
#         self.block_y=100
#         self.block=pygame.image.load("Snake/resources/block.jpg").convert()
#         self.direction='down'
    
    
#     def move_up(self):
#         self.direction='up'
#         # self.block_y=self.block_y-10
#         # self.draw()
#     def move_down(self):
#         self.direction='down'
#         # self.block_y=self.block_y+10
#         # self.draw()
#     def move_right(self):
#         self.direction='right'
#         # self.block_x=self.block_x+10
#         # self.draw()
#     def move_left(self):
#         self.direction='left'
#         # self.block_x=self.block_x-10
#         # self.draw()
#     def walk(self):
#         if  self.direction=='up':
#             self.block_y+=10
#         if  self.direction=='down':
#             self.block_y-=10
#         if  self.direction=='left':
#             self.block_x-=10
#         if  self.direction=='right':
#             self.block_x+=10
#         self.draw()

#     def draw(self):

#         self.parent_screen.fill((73, 196, 155))
#         self.parent_screen.blit(self.block,(self.block_x,self.block_y))
#         pygame.display.flip()


# class Game:
#     def __init__(self):
#         pygame.init()
#         self.surface=pygame.display.set_mode((500,500))

#         self.snake=Snake(self.surface)
#         self.snake.draw()
#     def run(self):
#         running=True



                
        
#         while running:
#          for event in pygame.event.get():
#             if  event.type==KEYDOWN:
#                 if event.key==K_ESCAPE:
#                     running=False
#                 if event.key==K_UP:
#                     self.snake.move_up()
#                 if event.key==K_DOWN:
#                     self.snake.move_down()
#                 if event.key==K_RIGHT:
#                     self.snake.move_right()
#                 if event.key==K_LEFT:
#                    self.snake.move_left()
#             elif event.type==QUIT:
#                 running=False

#         self.snake.walk()
#         time.sleep(0.2)
    
# if __name__=="__main__":
#     game=Game()
#     game.run()

   
    


from typing import Sized
import pygame
from pygame.locals import *
import time
import random
SIZE=40
class Apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.x=SIZE*3
        self.y=SIZE*3
        self.image=pygame.image.load("Snake/resources/apple.jpg").convert()
    def draw(self):
         self.parent_screen.blit(self.image,(self.x, self.y))
         pygame.display.flip()
    def move(self):
        self.x=random.randint(1,19)*SIZE
        self.y=random.randint(1,19)*SIZE

        
class Snake:
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Snake/resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'
    def increase_len(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()


    def draw(self):
        self.parent_screen.fill((145, 50, 168))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()
        #When snake collides with itself
        for i in range(2,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                print("Game over")
                exit(0)
        
    def display_score(self):
        font=pygame.font.SysFont("arial",30)
        score=font.render(f"Score:{self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(800,100))
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
                self.snake.increase_len()
                self.apple.move()
    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<=x2+SIZE:
            if y1>=y2 and y1<=y2+SIZE:
                return True
        return False
        
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            
            self.play()
            time.sleep(0.2)

if __name__ == '__main__':
    game = Game()
    game.run()



