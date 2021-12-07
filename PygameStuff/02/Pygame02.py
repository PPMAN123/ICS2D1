""" 
Show how Surface colours can be manipulated.
"""
import time

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
                    colourR = colour[0]
                    colourG = colour[1]
                    colourB = colour[2]
                    if colourR < 255:
                        colourR += 1
                    if colourR > 255:
                        colourR -= 1
                    if colourG < 228:
                        colourG += 1
                    if colourG > 228:
                        colourG -= 1
                    if colourB < 225:
                        colourB += 1
                    if colourB > 225:
                        colourB -= 1
                    colour = (colourR, colourG, colourB)
                    time.sleep(0.001)
                    background.fill(colour) #refill the background with the new colour
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                pygame.display.set_caption("RED!")
                #Fade the background colour to black once game loop is done
            elif ev.key == K_g:    
                colour = background.get_at((0,0)) #get the colour on the background Surface
                while colour != (220,220,220):
                    colourR = colour[0]
                    colourG = colour[1]
                    colourB = colour[2]
                    if colourR < 220:
                        colourR += 1
                    if colourR > 220:
                        colourR -= 1
                    if colourG < 220:
                        colourG += 1
                    if colourG > 220:
                        colourG -= 1
                    if colourB < 220:
                        colourB += 1
                    if colourB > 220:
                        colourB -= 1
                    colour = (colourR, colourG, colourB)
                    time.sleep(0.001)
                    background.fill(colour) #refill the background with the new colour
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                pygame.display.set_caption("GREEN!")
            elif ev.key == K_b:    
                colour = background.get_at((0,0)) #get the colour on the background Surface
                while colour != (150,205,205):
                    colourR = colour[0]
                    colourG = colour[1]
                    colourB = colour[2]
                    if colourR < 150:
                        colourR += 1
                    if colourR > 150:
                        colourR -= 1
                    if colourG < 205:
                        colourG += 1
                    if colourG > 205:
                        colourG -= 1
                    if colourB < 205:
                        colourB += 1
                    if colourB > 205:
                        colourB -= 1
                    colour = (colourR, colourG, colourB)
                    time.sleep(0.001)
                    background.fill(colour) #refill the background with the new colour
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                pygame.display.set_caption("BLUE!")    
            else:
                key_label = ev.unicode
                pygame.display.set_caption(str(key_label)*10)


    screen.blit(background, (0, 0))
    pygame.display.flip()