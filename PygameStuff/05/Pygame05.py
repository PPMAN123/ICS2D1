""" 
Basic editing of an image through mouse clicks
"""
import pygame
from pygame.locals import * 
pygame.init()

img = pygame.image.load("lorikeet.bmp") #load an image as a Surface

screen = pygame.display.set_mode((img.get_width() + 100, img.get_height())) #using image's size to determine the window size

#making the palette surfaces, and using the image's height to determine the height of the palettes
paletteRed = pygame.Surface((100,img.get_height()//3)).convert()
paletteGreen = pygame.Surface((100,img.get_height()//3)).convert()
paletteBlue = pygame.Surface((100,img.get_height()//3)).convert()

#filling the palettes with appropriate colours
paletteRed.fill((255,0,0))
paletteGreen.fill((0,255,0))
paletteBlue.fill((0,0,255))

#using width and height to do math to position the palettes properly
width = img.get_width()
height = img.get_height()//3
screen.blit(paletteRed, (width, 0))
screen.blit(paletteGreen, (width, height))
screen.blit(paletteBlue, (width, 2*height))


pygame.display.set_caption("Drag the mouse to draw!")

img = img.convert() #need to convert it after we have set-up the screen

#the display will not change, so we can blit & flip the display just once first
screen.blit(img, (0,0))
pygame.display.flip()


clock = pygame.time.Clock()
keep_going = True

#sets a default colour variable which will be changed later depending on what the user chooses
colour = (255,255,255)

prev_pos = (-1,-1)
while keep_going:
    clock.tick(30)
        
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        if ev.type == MOUSEBUTTONDOWN:
            x = ev.pos[0]
            y = ev.pos[1]
            if x >= width and y <= height:
                #if the user clicks in the red palette
                colour = (255,0,0)
            elif x >= width and y <= 2*height:
                #if the user clicks in the green palette
                colour = (0,255,0)
            elif x >= width:
                #if the user clicks in the blue palette
                colour = (0,0,255)
    if pygame.mouse.get_pressed()[0]: #if left mouse is pressed
        if prev_pos == (-1,-1):
            #first point
            prev_pos = pygame.mouse.get_pos()
        else:
            new_pos = pygame.mouse.get_pos()
            #the colour gets put into this function
            pygame.draw.line(img, colour, prev_pos, new_pos) #See the 'draw' module
            prev_pos = new_pos
    else:
        prev_pos = (-1,-1)
    screen.blit(img, (0,0))
    pygame.display.flip()
