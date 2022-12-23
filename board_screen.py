import pygame


class BoardScreen:
    """Render a Board to PyGame's screen, process input."""

    # width/height of chess piece images
    square_size = 60

    dark_square_color = 138, 120, 93
    light_square_color = 252, 204, 116

    dark_bishop = pygame.image.load("images/b.png")
    light_bishop = pygame.image.load("images/B.png")
    dark_rook = pygame.image.load("images/r.png")
    light_rook = pygame.image.load("images/R.png")
    dark_knight = pygame.image.load("images/n.png")
    light_knight = pygame.image.load("images/N.png")
    dark_king = pygame.image.load("images/k.png")
    light_king = pygame.image.load("images/K.png")
    dark_queen = pygame.image.load("images/q.png")
    light_queen = pygame.image.load("images/Q.png")
    dark_pawn = pygame.image.load("images/p.png")
    light_queen = pygame.image.load("images/P.png")

    def get_piece_image(self, piece_code):
        piece_name = {
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
        }[piece_code]
        return getattr(self, piece_name)

    def __init__(self, board, screen):
        self.board = board
        self.screen = screen

    def render(self):
        self.draw_board()
        self.draw_pieces()
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
