import pygame
from pygame.locals import *
from pathlib import Path
import sys
import random


# 1 - Define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
pathToBall = 'D:/Python/OOP-PyGame/PyOne-Image/images/avatar.gif'


BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
# 2 - Initialize World

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 3 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('D:/Python/OOP-PyGame/PyOne-Image/images/avatar.gif')

# 4 - Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
# 5 - Loop forever
while True:
    
    # 6 - Check for and handle events
    for event in pygame.event.get():
        #clicked the close button? Quit pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    # 7 - Do any "per frame" actions
    
    # 8 - Clear the window
    window.fill(BLACK)
    
    # 9 - Draw all window elements
    window.blit(ballImage, (ballX, ballY))
    
    # 10 - Update the window
    pygame.display.update()
    
    # 11 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
    
