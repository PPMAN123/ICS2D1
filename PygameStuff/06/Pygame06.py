""" 
A basic program with sample code for drawing shapes
"""
#make a new file and save it as pygame_shapes.py
import pygame
from pygame.locals import *
pygame. init()

size = (640, 480)
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
background.fill("#87ceeb")
screen.blit(background, (0,0))
pygame.display.set_caption("Pink Church")

#Polygons
#pygame.draw.polygon(screen, colour, all the points)
#Pay special attention to the number of brackets!

#pentagon for the base of the church
pygame.draw.polygon(screen, "#cb4154", ((320, 50), (640,240), (640, 480), (0,480), (0, 240)))

#Rectangles
#pygame.draw.rect(screen, colour, (x, y, width, height))

#door
pygame.draw.rect(screen, "#2e241b", (270, 280, 100, 200))

#Circles
#pygame.draw.circle(screen, colour, (x,y), radius)

#window on the top
pygame.draw.circle(screen, "#FFFFF7", (320, 150), 50)

#doorknob
pygame.draw.circle(screen, (0,0,0), (360, 380), 10)

#Lines
#pygame.draw.line(screen, colour, (x1,y1), (x2, y2), linewidth)

#window crosses
pygame.draw.line(screen, (0,0,0), (270,150), (370,150), 5)
pygame.draw.line(screen, (0,0,0), (320,100), (320,200), 5)

#door crosses
pygame.draw.line(screen, (0,0,0), (270,380), (350,380), 5)
pygame.draw.line(screen, (0,0,0), (320,280), (320,480), 5)

#cross
pygame.draw.line(screen, "#cb4154", (320,0), (320,51), 5)
pygame.draw.line(screen, "#cb4154", (300,25), (340,25), 5)


pygame.display.flip()

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
