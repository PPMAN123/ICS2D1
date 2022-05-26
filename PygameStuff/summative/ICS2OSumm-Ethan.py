""" 
A demo with multiple sprites, groups, and collisions
"""
import random
import pygame
from pygame.locals import * 
pygame.init()
#Start of game
screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size()).convert()
background.fill((0,255,255))
screen.blit(background, (0,0))
clock = pygame.time.Clock()



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pill.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = random.randrange(0,screen.get_width()-self.rect.width)
    def update(self, speed):
        self.rect.move_ip(0,speed)
    def die(self):
        self.kill()


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("newmouth.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = 320-(self.rect.width/2)
        self.rect.top = 480-self.rect.height
    def update(self, x):
        if x == -1 and not self.rect.bottomleft[0] <= 0:
            self.rect.left -= 3
        elif x == -2:
            if not self.rect.bottomleft[0] - 120 <= 0:
                self.rect.left -= 120
        elif x == 1 and not self.rect.bottomright[0] >= screen.get_width():
            self.rect.left += 3
        elif x == 2:
            if not self.rect.bottomright[0] + 120 >= screen.get_width():
                self.rect.left += 120

def main_menu():
    keep_going = True
    global game_status
    game_status = False
    while keep_going:
        clock.tick(30)
        menuBackground = pygame.Surface(screen.get_size()).convert()
        startButton = pygame.Surface((200,50)).convert()
        menuBackground.fill((255,255,255))
        font = pygame.font.SysFont('arial', 48)
        text = font.render("Start", True, (0,255,255))
        screen.blit(menuBackground, (0,0))
        screen.blit(startButton, ((screen.get_width()/2)-startButton.get_width()/2, 200))
        screen.blit(text, (((screen.get_width()/2)-startButton.get_width()/2) + ((startButton.get_width()/2) - (text.get_width()/2)),200))
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
            if ev.type == MOUSEBUTTONDOWN:
                x = ev.pos[0]
                y = ev.pos[1]
                if x >= ((screen.get_width()/2)-startButton.get_width()/2) and x <= ((screen.get_width()/2)-startButton.get_width()/2) + 200:
                    if y >= 200 and y <= 250:
                        game_status = True
                        game()
        pygame.display.flip()




ball_group = pygame.sprite.Group()


def game():
    text_font = pygame.font.SysFont("comic sans", 26)
    continue_game = True
    ball_group.add(Ball())
    block = Block()
    lives = 3
    counter = 0
    score = 0
    speed = 5
    secondaryCounter = 0
    condition = 30
    while game_status and continue_game and lives > 0:
        counter += 1
        secondaryCounter += 1
        clock.tick(30)
        keys = pygame.key.get_pressed()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                continue_game = False
            if ev.type == MOUSEBUTTONDOWN:
                if keys[K_a]:
                    block.update(-2)
                if keys[K_d]:
                    block.update(2)
        if keys[K_a]:
            block.update(-1)
        elif keys[K_d]:
            block.update(1)
        for ball in ball_group:
            if ball.rect.colliderect(block.rect):
                ball.die()
                score += 10
            if ball.rect.bottomleft[1] >= screen.get_height():
                splat = pygame.mixer.Sound("splat.wav")
                ball.kill()
                splat.play()
                lives -= 1
        if lives <= 0:
            continue_game = False
        gameBackground = pygame.Surface(screen.get_size()).convert()
        gameBackground.fill((255,255,255))
        screen.blit(gameBackground, (0,0))
        if secondaryCounter == 450:
            speed += 1
            secondaryCounter = 0
            condition -= 1
        ball_group.update(speed)
        ball_group.draw(screen)
        screen.blit(block.image, block.rect)
        livesDisplay = 'Lives: ' + str(lives)
        livesShow = text_font.render(livesDisplay, True, (0,0,0))
        scoreDisplay = 'Score: ' + str(score)
        scoreShow = text_font.render(scoreDisplay, True, (0,0,0))
        screen.blit(livesShow, (0,0))
        screen.blit(scoreShow, (screen.get_width() - scoreShow.get_size()[0],0))
        if counter >= condition:
            ball_group.add(Ball())
            counter = 0
        pygame.display.flip()

main_menu()
