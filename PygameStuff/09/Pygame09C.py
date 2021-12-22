""" 
Text input on a Surface
"""
import pygame
from pygame.locals import * 
pygame.init()

#made more space on screen for displaying
screen = pygame.display.set_mode((400, 200))
background = pygame.Surface(screen.get_size()).convert()
background.fill("#00008B") 

field_surf = pygame.Surface((390,50)).convert()
field_surf.fill((255,255,255))

#creating a second surface for the text to display on
secondFieldSurf = pygame.Surface((390, 100)).convert()
secondFieldSurf.fill((255,255,255))

my_font = pygame.font.SysFont("helvetica", 20)
#new fancy font
fancy_font = pygame.font.Font("cs_regular.ttf", 35)

#itallicize and underline to make it look better.
fancy_font.set_italic(True)
fancy_font.set_underline(True)

field_value = ""
field = my_font.render(field_value, True, (0,0,0))

#renders the second field using the regular field value
secondField = fancy_font.render(field_value, True, (0,0,0))

clock = pygame.time.Clock()
keepGoing = True
while keepGoing:
    clock.tick(30)    
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keepGoing = False
        elif ev.type == KEYDOWN:
            if ev.key == K_BACKSPACE and len(field_value) > 0:
                field_value = field_value[:-1] #cut off last character
            elif (ev.unicode.isalnum() or ev.key==K_SPACE) and len(field_value) < 20:
                field_value += ev.unicode #adds character value of key
            field = my_font.render(field_value, True, (0,0,0))
            #just rerenders the second field
            secondField = fancy_font.render(field_value, True, (0,0,0))

    screen.blit(background, (0, 0))
    screen.blit(field_surf, (5, 5))
    screen.blit(field, (60, 20))
    #extra blitting for the new values
    screen.blit(secondFieldSurf, (5, 85))
    screen.blit(secondField, (10, 120))
    pygame.display.flip()
