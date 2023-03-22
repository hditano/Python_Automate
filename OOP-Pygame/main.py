import pygame
from pygame.locals import *
import sys

# 1 - Define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 2 - Initialize World

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 3 - Load assets: image(s), sound(s), etc.

# 4 - Initialize variables

# 5 - Loop forever
while True:
    
    # 6 - Check for and handle events
    for event in pygame.event.get():
        #clicked the close button? Quit pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # 7 - Do any "per frame" actions
    
    # 8 - Clear the window
    window.fill(BLACK)
    
    # 9 - Draw all window elements
    
    # 10 - Update the window
    pygame.display.update()
    
    # 11 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
    
