""" 
Respond to keyboard without events
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

clock = pygame.time.Clock()
keep_going = True

while keep_going:
    clock.tick(30)
    pygame.event.pump() #need to call once per loop when not using event handling 
    keys = pygame.key.get_pressed()
    print(len(keys), keys)
    if keys[K_ESCAPE]:
        keep_going = False
    if keys[K_r]:
        background.fill((255, 0, 0))
        pygame.display.set_caption("RED!")  
    elif keys[K_g]:
        background.fill((0, 255, 0))
        pygame.display.set_caption("GREEN!")
    elif keys[K_b]:
        background.fill((0, 0, 255))
        pygame.display.set_caption("BLUE!")
    elif keys[K_o]:
        background.fill((255, 165, 0))
        pygame.display.set_caption("ORANGE!")
    elif keys[K_y]:
        background.fill((255,255,0))
        pygame.display.set_caption("YELLOW!")
    elif keys[K_i]:
        background.fill((75,0,130))
        pygame.display.set_caption("INDIGO!")
    elif keys[K_p]:
        background.fill((128,0,128))
        pygame.display.set_caption("PURPLE!")

    screen.blit(background, (0, 0))
    pygame.display.flip()
