""" 
Basic animation/movement of an image Surface
"""
import pygame
from pygame.locals import * 
import random
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

#variables to see if the image has to move back
moveBackTopLeft = False
moveBackTopRight = False
moveBackLeft = False

#checks how many directions the image has moved
timesLoaded = 0

#checks if the image has moved back left
leftRightCounter = 0


while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False

    if timesLoaded == 2:
        #final movement left to right
        if not moveBackLeft and img_rect.topleft[0] == 0:
            leftRightCounter += 1
        if img_rect.topleft[0] < 640 and not moveBackLeft:
            #if the image is not supposed to move back, it's moving forwards to the right side.
            img_rect.left += 1
        if img_rect.topright[0] > 640:
            #if the image has reached the right side, it triggers moveBackLeft to move the image back left
            moveBackLeft = True
            leftRightCounter += 1
        if moveBackLeft:
            #moves the image back left
            img_rect.left -= 1
        if img_rect.topleft[0] <= 0 and leftRightCounter == 2:
            #stops program if the image goes right and comes back left
            keep_going = False
    elif timesLoaded == 1:
        #second movement; top right to bottom left
        if img_rect.bottomleft[0] > 0 and not moveBackTopRight:
            #if the image has not moved to the bottom left, it keeps going there
            img_rect.top += 1
            img_rect.left -= 1
        else:
            #if it has moved to the bottom left, it is now moving back up triggering the moveBackTopRight variable
            img_rect.top -= 1
            img_rect.left += 1
            moveBackTopRight = True
        if img_rect.left > 140 or img_rect.top < 0:
            #if it has returned to the top right corner, it is going to send the image to a random spot on the left side of the screen.
            moveBackTopRight = False
            img_rect.top = random.randint(0,480 - img.get_height())
            img_rect.left = 0
            timesLoaded += 1
    else:
        #first movement; top left to bottom right
        if img_rect.topleft[0] < 0 or img_rect.topleft[1] < 0:
            #if the image has returned to the top right, it sends it to the left corner
            moveBackTopLeft = False
            img_rect.top = 0
            img_rect.left = 140
            timesLoaded += 1
        if img_rect.bottomright[0] < 640 and not moveBackTopLeft:
            #if the image has not moved to the bottom right, it keeps going
            img_rect.top += 1
            img_rect.left += 1
        else:
            #if the image has moved to the bottom right, it goes back up to the top left, and triggering the moveBackTopLeft variable
            img_rect.top -= 1
            img_rect.left -= 1
            moveBackTopLeft = True
    


    screen.blit(background, (0,0)) #UNCOMMENT THIS TO ELIMINATE 'STREAKS'
    screen.blit(img, img_rect)
    pygame.display.flip()
