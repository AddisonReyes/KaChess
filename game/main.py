import pygame

from .chess_board import ChessBoard


def game(second_screen: bool = False):
    pygame.init()

    display_index = 0
    if second_screen and pygame.display.get_num_displays() > 1:
        display_index = 1

    screen = pygame.display.set_mode((8 * 64 + 64, 8 * 64 + 64), display=display_index)
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
        screen.fill("grey16")

        # RENDER YOUR GAME HERE
        cb.display_board(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
