""" 
Basic animation/movement of an image Surface
"""
import pygame
from pygame.locals import * 
pygame.init()

screen = pygame.display.set_mode((640, 480))
img = pygame.image.load("lorikeet.bmp").convert()
img_rect = img.get_rect()

background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))
screen.blit(background, (0,0))
screen.blit(img, img_rect)

clock = pygame.time.Clock()
keep_going = True
moveBackTopLeft = False
moveBackTopRight = False
timesLoaded = 0

while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
    if timesLoaded == 1:
        if img_rect.topright[0] > 640 or img_rect.topright[1] < 0:
            moveBackTopRight = False
            img_rect.top = 0
            img_rect.left = 0
            timesLoaded += 1
            print(img_rect.topleft)
        if img_rect.bottomleft[0] > 0 and not moveBackTopRight:
            img_rect.top += 1
            img_rect.left -= 1
        else:
            img_rect.top -= 1
            img_rect.left += 1
            moveBackTopRight = True
    else:
        if img_rect.topleft[0] < 0 or img_rect.topleft[1] < 0:
            moveBackTopLeft = False
            img_rect.top = 0
            img_rect.left = 140
            timesLoaded += 1
            print(img_rect.topright)
        if img_rect.bottomright[0] < 640 and not moveBackTopLeft:
            img_rect.top += 1
            img_rect.left += 1
        else:
            img_rect.top -= 1
            img_rect.left -= 1
            moveBackTopLeft = True
    


    screen.blit(background, (0,0)) #UNCOMMENT THIS TO ELIMINATE 'STREAKS'
    screen.blit(img, img_rect)
    pygame.display.flip()
