import os

import pygame

from board.flexible_board import Move

PIECE_NAME = {
    "b": "dark_bishop",
    "B": "light_bishop",
    "r": "dark_rook",
    "R": "light_rook",
    "n": "dark_knight",
    "N": "light_knight",
    "k": "dark_king",
    "K": "light_king",
    "q": "dark_queen",
    "Q": "light_queen",
    "p": "dark_pawn",
    "P": "light_queen",
}


class BoardScreen:
    """Render a Board to PyGame's screen, process input."""

    # width/height of chess piece images
    square_size = 60

    dark_square_color = 138, 120, 93
    light_square_color = 252, 204, 116

    def _set_image_attrs(self):
        _dir = os.path.dirname(__file__)

        setattr(
            self,
            "move_target_image",
            pygame.image.load(f"{_dir}/images/move-target.png"),
        )

        for piece_code, piece_name in PIECE_NAME.items():
            setattr(
                self, piece_name, pygame.image.load(f"{_dir}/images/{piece_code}.png")
            )

    def get_piece_image(self, piece_code):
        piece_name = PIECE_NAME[piece_code]
        return getattr(self, piece_name)

    def __init__(self, board, screen):
        self._set_image_attrs()
        self.board = board
        self.screen = screen
        self.square_from = None

    def render(self):
        self.draw_board()
        self.draw_pieces()
        self.draw_picked_up_piece()
        pygame.display.flip()

    def draw_board(self):
        for board_rank in range(self.board.ranks):
            for board_file in range(self.board.files):

                color = self.dark_square_color
                if (board_rank + board_file) % 2 == 0:
                    color = self.light_square_color

                # highlight current square
                square = board_file + self.board.files * board_rank
                if square == self.current_square:
                    color = tuple(
                        (255 + rgb) / 2 for rgb in color  # 50/50 mix color with white
                    )

                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        0 + board_file * self.square_size,
                        0 + board_rank * self.square_size,
                        self.square_size,
                        self.square_size,
                    ),
                )

    def draw_pieces(self):
        for index, piece_code in enumerate(self.board.squares):

            if not piece_code:
                continue  # empty square

            # calculate rank and file
            board_file = index % self.board.files
            board_rank = index // self.board.files

            # Don't draw piece if it's being moved
            if index == self.square_from:
                continue

            piece_image = self.get_piece_image(piece_code)

            rect = piece_image.get_rect().move(
                board_file * self.square_size, board_rank * self.square_size
            )
            self.screen.blit(piece_image, rect)

    def draw_picked_up_piece(self):
        if not self.square_from:
            return

        piece_code = self.board.squares[self.square_from]
        if not piece_code:
            return

        piece_image = self.get_piece_image(piece_code)

        x = self.pos[0] - self.square_size / 2
        y = self.pos[1] - self.square_size / 2
        move_piece_rect = piece_image.get_rect().move(x, y)

        self.screen.blit(piece_image, move_piece_rect)

    def handle(self, event):
        """Handle user input."""
        x, y = event.pos
        file_index = x // self.square_size
        rank_index = y // self.square_size
        square = file_index + self.board.files * rank_index

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.square_from = square

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.square_from == square:
                # no move
                pass
            else:
                move = Move(self.square_from, square)
                self.board.push(move)
            self.square_from = None

        elif event.type == pygame.MOUSEMOTION:
            self.pos = event.pos
            self.current_square = square

        else:
            raise RuntimeError("Unknown event type")

        self.render()
