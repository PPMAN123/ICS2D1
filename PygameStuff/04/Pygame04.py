""" 
Exploring basic Surfaces and colours
"""
import pygame
from pygame.locals import * 
import random
pygame.init()

full_size = (640, 480) #full screeen size
bar_size = (640, 80)   #size of each colour bar
screen = pygame.display.set_mode(full_size)

background = pygame.Surface(full_size).convert()
bg_colour = (0, 0, 0) #it helps to have the colour as a separate variable
background.fill(bg_colour)
pygame.display.set_caption("Colour: " + str(bg_colour)) #our caption will change

#Create the three colour bars


clock = pygame.time.Clock()
keep_going = True
red_bar = pygame.Surface(bar_size).convert()
green_bar = pygame.Surface(bar_size).convert()
blue_bar = pygame.Surface(bar_size).convert()
#initializes the default colours
currentBarOneColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
currentBarTwoColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
currentBarThreeColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
currentBarFourColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
#initalizes the background and gives it a default colour
red_bar.fill(currentBarOneColour)
green_bar.fill(currentBarTwoColour)
blue_bar.fill(currentBarThreeColour)
background.fill(currentBarFourColour)

#booleans to keep track of if the bars are getting frozen
freezeR = False
freezeG = False
freezeB = False
freezeBackground = False

while keep_going:
    clock.tick(10)
    keys = pygame.key.get_pressed()
    #checks if the bars should be frozen, if they should not, generate new colours.
    if not freezeR:
        currentBarOneColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if not freezeG:
        currentBarTwoColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if not freezeB:
        currentBarThreeColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if not freezeBackground:
        currentBarFourColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        elif ev.type == MOUSEBUTTONDOWN: #A mouse click!
            x = ev.pos[0]  #the MOUSEBUTTONDOWN event has a position property
            y = ev.pos[1]  #that is an (x, y) tuple
            #Determine the bar that was clicked by checking the y-coordinate
            #if the bar has been clicked, turn the freeze booleans to true to stop genereating new colours
            if y >= 0 and y < 80:   #we hit the red bar
                freezeR = True
            elif y >= 80 and y < 160:   #we hit the green bar
                freezeG = True
            elif y >= 160 and y < 240:   #we hit the blue bar
                freezeB = True
            elif y >= 240 and y < 480:
                freezeBackground = True
    #fills the bars with the appropriate colours
    background.fill(currentBarFourColour)
    red_bar.fill(currentBarOneColour)
    green_bar.fill(currentBarTwoColour)
    blue_bar.fill(currentBarThreeColour)
    #sets the bars to black when space bar is clicked
    if keys[K_SPACE]:
        background.fill((0,0,0))
        red_bar.fill((0,0,0))
        green_bar.fill((0,0,0))
        blue_bar.fill((0,0,0))
    #Here we blit multiple surfaces. Order is important if overlapping.
    screen.blit(background, (0, 0))
    screen.blit(red_bar, (0, 0))
    screen.blit(green_bar, (0, 80))  #Note how we have to adjust the top-right corner
    screen.blit(blue_bar, (0, 160))
    pygame.display.flip()
