""" 
Testing out Fonts
"""
import pygame
from pygame.locals import * 
pygame.init()

screen = pygame.display.set_mode((400, 200))
background = pygame.Surface(screen.get_size()).convert()
background.fill((0, 0, 0))

my_font = pygame.font.Font("Pacifico.ttf", 60) #custom font, needs font file

my_font2 = pygame.font.SysFont("notomono", 48) #system fonts, needs font name
print(pygame.font.get_fonts()) #gets a list of all valid system font names

my_font2.set_bold(True)
my_font2.set_underline(True)
my_font2.set_italic(True)

label = my_font.render("Pygame!", False, (255,0,0))
label2 = my_font2.render("Pygame!", True, (0,0, 255))
screen.blit(background, (0,0))
screen.blit(label, (60, 20))
screen.blit(label2, (60, 80))
pygame.display.flip()

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
