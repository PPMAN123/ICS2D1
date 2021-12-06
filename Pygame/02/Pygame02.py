""" 
Show how Surface colours can be manipulated.
"""

import pygame
from pygame.locals import * 
pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Yeah, Pygame!")

background = pygame.Surface(size)
background = background.convert()
background.fill((0, 0, 0))

clock = pygame.time.Clock()
keep_going = True

while keep_going:
    clock.tick(30)
        
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        elif ev.type == KEYDOWN:
            if ev.key == K_r:
                colour = background.get_at((0,0)) #get the colour on the background Surface
                while colour != (255,228,225):
                    colour = (min(colour[0]+1,255), min(colour[1]+1,255), min(colour[2]+1,255))
                    background.fill(colour) #refill the background with the new colour
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                pygame.display.set_caption("RED!")
                #Fade the background colour to black once game loop is done
            elif ev.key == K_g:    
                colour = background.get_at((0,0)) #get the colour on the background Surface
                while colour != (220,220,220):
                    colour = (max(colour[0]-1,0), max(colour[1]+1,0), max(colour[2]-1,0))
                    background.fill(colour) #refill the background with the new colour
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                pygame.display.set_caption("GREEN!")
            elif ev.key == K_b:    
                colour = background.get_at((0,0)) #get the colour on the background Surface
                while colour != (150,205,205):
                    colour = (max(colour[0]-1,0), max(colour[1]-1,0), max(colour[2]+1,0))
                    background.fill(colour) #refill the background with the new colour
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                pygame.display.set_caption("BLUE!")    
            else:
                key_label = ev.unicode
                pygame.display.set_caption(str(key_label)*10)


    screen.blit(background, (0, 0))
    pygame.display.flip()
    

