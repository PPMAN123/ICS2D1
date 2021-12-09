""" 
Basic animation/movement of an image Surface
"""
import pygame
from pygame.locals import * 
pygame.init()

screen = pygame.display.set_mode((640, 480))
img = pygame.image.load("ball.bmp").convert()
sound = pygame.mixer.Sound("bounce.wav")
img_rect = img.get_rect()
img_rect.left = 1
img_rect.top = 1

background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))

dir_x = 1 #1 means right, -1 means left
dir_y = 1 #1 means down, -1 means up
speed = 3

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)
    keys = pygame.key.get_pressed()
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
    if keys[K_DOWN] and speed > 1:
        speed -= 1
    if keys[K_UP]:
        speed += 1
	
    #Handling the walls for some bounce
    if img_rect.right >= screen.get_width() or img_rect.left <= 0:
        sound.play()
        dir_x *= -1
    if img_rect.bottom >= screen.get_height() or img_rect.top <= 0:
        sound.play()
        dir_y *= -1

    #update the position
    img_rect.move_ip(speed*dir_x, speed*dir_y)

    screen.blit(background, (0,0)) 
    screen.blit(img, img_rect)
    pygame.display.flip()