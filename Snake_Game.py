import pygame
from pygame.locals import *
import random

pygame.init()

width = 500
height = 500

red = (255, 0, 0)
yellow = (255, 255, 0)
colour_state = False
colour = red

step = 20
x = (width - step)/2
y = (height - step)/2
vel = 20
changeX = 0
changeY = 0

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

running = True

clock = pygame.time.Clock()


class Snake:
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
        self.body = [[self.x,self.y],[self.x,self.y+20]]
        self.head = self.body[0]

    def move(self,changeX,changeY):
   
        for x in range((self.length-1),0,-1):
            self.body[x][0] = self.body[x-1][0]
            self.body[x][1] = self.body[x-1][1]

        self.body[0][0] += changeX
        self.body[0][1] += changeY
            
    
    def extend(self): 
        self.body.append([self.body[self.length-1][0], (self.body[self.length-1][1]) + 20])
        self.length += 1

    def body_crash(self):
        for x in range(2,self.length):
            if self.body[0][0] == self.body[x][0]:
                if self.body[0][1] == self.body[x][1]:
                    pygame.quit()
                    quit()
 
    def draw(self):
        for i in range(self.length):
            pygame.draw.rect(window, (255,0,0), pygame.Rect(self.body[i][0], self.body[i][1], 20, 20))

        
class Food:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 20

    def update_pos(self, width, height):
        self.x = random.randrange(20, width - 20, 20)
        self.y = random.randrange(20, height - 20, 20)


    def draw(self):
        pygame.draw.rect(window, (0,255,0), pygame.Rect(self.x, self.y, self.size, self.size))


def detect_hit(x1,y1,x2,y2):
    tol = 5
    if abs(x1 - x2) < tol and abs(y1 - y2) < tol:
        fruit.update_pos(width,height)
        snake.extend()

def border_crash(x1,y1,width, height):
    if x1 == 0 or x1 == (width-20) or y1 == 0 or y1 == (height-20):
        pygame.quit()
        quit()


snake = Snake(x,y,2) 
fruit = Food(60, 60)
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -vel
                changeY = 0
            elif event.key == pygame.K_RIGHT:
                changeX = vel
                changeY = 0
            elif event.key == pygame.K_UP:
                changeX = 0
                changeY = -vel
            elif event.key == pygame.K_DOWN:
                changeX = 0
                changeY = vel

    # check collision with window border
    
    detect_hit(snake.head[0],snake.head[1],fruit.x,fruit.y)
    snake.body_crash()
    border_crash(snake.head[0],snake.head[1],width,height)

    snake.move(changeX, changeY)
    

    window.fill((0, 0, 0))
    snake.draw()
    fruit.draw()
    pygame.display.flip()
    clock.tick(5)
    
    