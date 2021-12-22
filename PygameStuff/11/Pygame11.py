""" 
A demo with multiple sprites, groups, and collisions
"""
import random
import pygame
from pygame.locals import * 
pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #construct the parent component
        self.image = pygame.image.load("small_ball.png").convert_alpha()
        self.rect = self.image.get_rect() #loads the rect from the image

        #set the position, direction, and speed of the ball
        self.rect.left = random.randrange(0,screen.get_width()-self.rect.width)
        self.rect.top = random.randrange(0,screen.get_height()-self.rect.height)
        self.dir_x = random.choice([-1,1])
        self.dir_y = random.choice([-1,1])
        self.speed = random.randrange(1,4)


    def update(self):
        #Handle the walls by changing direction(s)
        if self.rect.left < 0 or self.rect.right >= screen.get_width():
            self.dir_x *= -1
        if self.rect.top < 0 or self.rect.bottom >= screen.get_height():
            self.dir_y *= -1
        self.rect.move_ip(self.speed*self.dir_x, self.speed*self.dir_y)

        
class Block(pygame.sprite.Sprite):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10)).convert()
        self.image.fill(colour)
        self.rect = self.image.get_rect()

        #set the position of the block
        self.rect.left = random.randrange(0,screen.get_width()-self.rect.width)
        self.rect.top = random.randrange(0,screen.get_height()-self.rect.height)
        
#Start of game
screen = pygame.display.set_mode((640, 480))

#make 8 balls and put them in a group called ball_group
ball_group = pygame.sprite.Group()
for i in range(8):
    ball_group.add(Ball())





#make 1000 blocks in random colours and a separate group for them called block_group
block_group = pygame.sprite.Group()
for i in range(1000):
    colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    block_group.add(Block(colour))




    
    
background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))
screen.blit(background, (0,0))

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False

            
    #for every ball in the group, check for collisions, killing the blocks hit
    pygame.sprite.groupcollide(ball_group, block_group, False, True)



        
    
    #stop the loop when all the blocks are gone
    if len(block_group) == 0:
        keep_going = False


            
    #Update the screen 
    ball_group.clear(screen, background)
    block_group.clear(screen, background)
    ball_group.update()
    block_group.draw(screen)
    ball_group.draw(screen)
    pygame.display.flip()