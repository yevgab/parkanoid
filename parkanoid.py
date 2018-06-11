# Project: Parkanoid. Breakout type game with a floral theme
#
# https://github.com/yevgab/parkanoid.git
#
# dr.doberman, yevgab
#
"""
Main game module
"""

import pygame

MIN_S_SIZE = (800, 600)

C_BKGROUND  = ( 18,  81,   9)

C_YELLOW  = (255, 255,   0)
C_CYAN    = (  0, 255, 255)
C_PINK    = (255,   0, 255)
C_ORANGE  = (255, 128,   0)
C_WHITE   = (255, 255, 255)

def run():
    """
    Runs application

    Intializes graphics and runs event loop
    """
    pygame.init()

    screen = pygame.display.set_mode(MIN_S_SIZE, pygame.DOUBLEBUF, 16)
    pygame.display.set_caption("Parkanoid")    
    
    clock = pygame.time.Clock()


    done = False

    while not done:

        # --- Main event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    break

        # Clear screen
        screen.fill(C_BKGROUND)

        # Renew frame in memory

        # Pull image from memory to display
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run()