""" 
A basic program with sample code for drawing shapes
"""
#make a new file and save it as pygame_shapes.py
import pygame
from pygame.locals import *
pygame. init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Drawing")

#Polygons
#pygame.draw.polygon(screen, colour, all the points)
#Pay special attention to the number of brackets!
pygame.draw.polygon(screen, (0,0,100), ((320, 0), (640,240), (640, 480), (0,480), (0, 240)))

#Rectangles
#pygame.draw.rect(screen, colour, (x, y, width, height))
pygame.draw.rect(screen, (255,255,255), (270, 280, 100, 200))

#Circlesw
#pygame.draw.circle(screen, colour, (x,y), radius)
pygame.draw.circle(screen, (150,0,0), (320, 150), 50)

#Lines
#pygame.draw.line(screen, colour, (x1,y1), (x2, y2), linewidth)
pygame.draw.line(screen, (20,150,20), (10,380), (500,300), 5)


pygame.display.flip()

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
