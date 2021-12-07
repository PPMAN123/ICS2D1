import pygame
from pygame.locals import *
pygame.init()
#initialization

size = (640, 480)
#sets the screen size
screen = pygame.display.set_mode(size)
#sets the display to the screen size
pygame.display.set_caption("Yeah, Pygame!")
#initializes a default caption

background = pygame.Surface(size)
background = background.convert()
background.fill((0, 0, 255))
#default colour of background

clock = pygame.time.Clock()
keep_going = True
#tracker to see if the program should keep running
while keep_going:
    clock.tick(30)
    #sets ticks per second
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
            #quits program when the x button is clicked
        elif ev.type == KEYDOWN:
            #sees if the event that happend was a key press
            if ev.key == K_r:
                #if the keypress was "r", it fills the background with red and changes the caption to RED!
                background.fill((255, 0, 0))
                pygame.display.set_caption("RED!")
            elif ev.key == K_g:
                #if the keypress is "g", it fills the background with green and changes the caption to GREEN!
                background.fill((0, 255, 0))
                pygame.display.set_caption("GREEN!")
            elif ev.key == K_b:
                #if the keypress is "b", it fills the background with blue and changes the caption to BLUE!
                background.fill((0, 0, 255))
                pygame.display.set_caption("BLUE!")    
            else:
                key_label = ev.unicode 
                pygame.display.set_caption(str(key_label)*10)
                #if the keypress is not r g or b, it will set the caption into the keypress 10 times
    screen.blit(background, (0, 0))
    pygame.display.flip()
