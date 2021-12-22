""" 
Basic Sprite version of our ball bouncer
"""

import pygame
from pygame.locals import * 
import random
pygame.init()
class Ball(pygame.sprite.Sprite):
    #made init function take in another variable for basketballs
    def __init__(self, imageLink):
        pygame.sprite.Sprite.__init__(self) #construct the parent component
        self.image = pygame.image.load(imageLink).convert()
        self.image.set_colorkey(self.image.get_at( (0,0) ))

        self.rect = self.image.get_rect() #loads the rect from the image

        #set the position, direction, and speed of the ball
        self.rect.topleft = (random.randint(100,600), random.randint(100,400))
        self.dir_x = 1
        self.dir_y = 1
        self.speed = 4	

    def update(self):
        #Handle the walls by changing direction(s)
        if self.rect.left < 0 or self.rect.right >= screen.get_width():
            self.dir_x *= -1
        if self.rect.top < 0 or self.rect.bottom >= screen.get_height():
            self.dir_y *= -1
        self.rect.move_ip(self.speed*self.dir_x, self.speed*self.dir_y)

    def adjust_speed(self, delta):
        self.speed += delta
        
screen = pygame.display.set_mode((640, 480))

#initializing 2 balls
ball = Ball("soccerball.bmp")
secondBall = Ball("basketball.jpg")

background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        elif ev.type == KEYDOWN:
            #Ability to increase/decrease speed
            if ev.key == K_UP:
                ball.adjust_speed(1)
            elif ev.key == K_DOWN:
                ball.adjust_speed(-1)
            elif ev.key == K_RIGHT:
                secondBall.adjust_speed(1)
            elif ev.key == K_LEFT:
                secondBall.adjust_speed(-1)
        
    ball.update()
    secondBall.update()
    screen.blit(background, (0,0))
    screen.blit(ball.image, ball.rect)
    #blitting another ball
    screen.blit(secondBall.image, secondBall.rect)
    pygame.display.flip()
