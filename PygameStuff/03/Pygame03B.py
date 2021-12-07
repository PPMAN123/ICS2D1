""" 
A basic program establishing a simple framework for future games.
"""

import pygame
from pygame.locals import *
pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Yeah, Pygame!")


background = pygame.Surface(size)
background = background.convert()
background.fill((0, 0, 255))
prevColour = (0,0,255)
prevCaption = "Yeah, Pygame!"

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        elif ev.type == KEYDOWN:
            if ev.key == K_r:
                background.fill((255, 0, 0))
                pygame.display.set_caption("RED!")
            elif ev.key == K_g:    
                background.fill((0, 255, 0))
                pygame.display.set_caption("GREEN!")
            elif ev.key == K_b:    
                background.fill((0, 0, 255))
                pygame.display.set_caption("BLUE!")    
            else:
                key_label = ev.unicode 
                pygame.display.set_caption(str(key_label)*10)
            prevColour = background.get_at((0,0))
            prevCaption = pygame.display.get_caption()
            print(prevCaption)
        elif ev.type == MOUSEBUTTONDOWN:
            background.fill((255,255,255))
            pygame.display.set_caption("SNOWSTORM!")
        elif ev.type == MOUSEBUTTONUP:
            background.fill(prevColour)
            pygame.display.set_caption(prevCaption[0])
            #I don't know why prevCaption becomes "Y" on the first run


    screen.blit(background, (0, 0))
    pygame.display.flip()
