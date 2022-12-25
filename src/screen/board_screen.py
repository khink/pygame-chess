import os

import pygame

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
        self.square_to_move = None

    def render(self):
        self.draw_board()
        self.draw_pieces()
        self.draw_possible_moves()
        pygame.display.flip()

    def draw_board(self):
        for board_rank in range(self.board.ranks):
            for board_file in range(self.board.files):

                color = self.dark_square_color
                if (board_rank + board_file) % 2 == 0:
                    color = self.light_square_color

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

            piece_image = self.get_piece_image(piece_code)
            rect = piece_image.get_rect().move(
                board_file * self.square_size, board_rank * self.square_size
            )
            self.screen.blit(piece_image, rect)

    def draw_possible_moves(self):
        """Draw the possible moves on the board if a piece was selected."""
        if not self.square_to_move:
            return

        board_rank, board_file = self.square_to_move

        for target_board_rank, target_board_file in self.board.get_valid_moves(
            board_rank, board_file
        ):
            move_target_rect = self.move_target_image.get_rect().move(
                target_board_file * self.square_size,
                target_board_rank * self.square_size,
            )

            self.screen.blit(self.move_target_image, move_target_rect)

    def handle(self, event):
        """Handle user input."""
        if event.type == pygame.MOUSEBUTTONUP:
            return
        x, y = event.pos
        board_file = x // self.square_size
        board_rank = y // self.square_size
        self.square_to_move = (board_rank, board_file)
        print(self.board)
