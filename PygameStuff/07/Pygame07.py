""" 
Basic animation/movement of an image Surface
"""
import pygame
from pygame.locals import * 
pygame.init()

screen = pygame.display.set_mode((640, 480))
img = pygame.image.load("lorikeet.bmp").convert()
img2 = pygame.image.load("lorikeet.bmp").convert()
img_rect = img.get_rect()
img2_rect = img2.get_rect()

img2_rect.top = 0
img2_rect.left = 140

background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))
screen.blit(background, (0,0))
screen.blit(img, img_rect)
screen.blit(img2, img2_rect)

clock = pygame.time.Clock()
keep_going = True
moveBackTopLeft = False
moveBackTopRight = False

while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
    if img_rect.topleft[0] < 0 or img_rect.topleft[1] < 0:
            moveBackTopLeft = False
    if img_rect.bottomright[0] < 640 and not moveBackTopLeft:
        img_rect.top += 1
        img_rect.left += 1
    else:
        img_rect.top -= 1
        img_rect.left -= 1
        moveBackTopLeft = True

    if img2_rect.topright[0] > 640 or img2_rect.topright[1] < 0:
            moveBackTopRight = False
    if img2_rect.bottomleft[0] > 0 and not moveBackTopRight:
        img2_rect.top += 1
        img2_rect.left -= 1
    else:
        img2_rect.top -= 1
        img2_rect.left += 1
        moveBackTopRight = True


    screen.blit(background, (0,0)) #UNCOMMENT THIS TO ELIMINATE 'STREAKS'
    screen.blit(img, img_rect)
    screen.blit(img2, img2_rect)
    pygame.display.flip()
