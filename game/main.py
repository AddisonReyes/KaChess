import os

import pygame

from .chess_board import ChessBoard

def game(second_screen: bool = False):
    pygame.init()

    if second_screen:
        desktop_sizes = pygame.display.get_desktop_sizes()
        if len(desktop_sizes) > 1:
            os.environ["SDL_VIDEO_WINDOW_POS"] = f"{desktop_sizes[0][0] + 40},40"

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    running = True

    cb = ChessBoard()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        cb.display_board(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
