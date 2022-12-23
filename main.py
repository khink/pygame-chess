import sys

import pygame

from board import Board
from board_screen import BoardScreen


pygame.init()
board = Board(6, 5)
screen = pygame.display.set_mode(
    (
        BoardScreen.square_size * board.files,
        BoardScreen.square_size * board.ranks,
    ),
)
board_screen = BoardScreen(board, screen)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type in [pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
            board_screen.handle(event)

        board_screen.render()
