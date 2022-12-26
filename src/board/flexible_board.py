def is_opposite_color(piece_code_one, piece_code_two):
    if piece_code_one.isupper():
        return piece_code_two.islower()
    return piece_code_two.isupper()


class FlexibleBoard:
    """A chess board with flexible dimensions.

    Keeps track where pieces are, and which moves are valid.

    Chess stuff only! Rendering / input goes in BoardScreen.
    """

    def __init__(self, fen):

        self._set_board_fen(fen)

    def _set_board_fen(self, fen):
        self.squares = []

        square_index = 0
        nr_of_files_in_rank = 0
        nr_of_ranks = 1
        for char in fen:
            if char == "/":
                if hasattr(self, "files"):
                    # TODO move fen validation to separate method
                    assert (
                        self.files == nr_of_files_in_rank
                    ), "This rank has a different number of squares than the other rank(s)"
                else:
                    self.files = nr_of_files_in_rank
                nr_of_ranks += 1
                nr_of_files_in_rank = 0
            else:
                if char.isdigit():
                    empty_squares = int(char)
                    [self.squares.append(None) for empty_square in range(empty_squares)]
                    square_index += empty_squares
                    nr_of_files_in_rank += empty_squares
                else:
                    self.squares.append(char)
                    square_index += 1
                    nr_of_files_in_rank += 1

        self.ranks = nr_of_ranks

    def __str__(self):
        builder = []

        for index, value in enumerate(self.squares):
            if not value:
                builder.append(".")
            else:
                builder.append(value)

            board_file = index % self.files
            if board_file == self.files - 1:
                builder.append("\n")
            else:
                builder.append(" ")

        return "".join(builder)

    def push(self, move):
        print(move)
        piece_code = self.squares[move.from_square]
        self.squares[move.to_square] = piece_code
        self.squares[move.from_square] = None

    def generate_pseudo_legal_moves(self, square):
        """Legal moves that might not move the king out of check."""

        piece_code = self.squares[square]
        if not piece_code:
            return []

        squares = []

        if piece_code in ["P", "p"]:
            if piece_code == "p":
                forward_square = square - self.files
            else:
                forward_square = square - self.files

            if (
                forward_square in range(len(self.squares))
                and not self.squares[forward_square]
            ):
                squares.append(forward_square)

            for offset in [-1, 1]:
                capture_square = forward_square + offset
                try:
                    occupying_piece_code = self.squares[capture_square]
                    if occupying_piece_code and is_opposite_color(
                        occupying_piece_code, piece_code
                    ):
                        squares.append(capture_square)
                except IndexError:
                    # pawn at edge of board
                    pass

        print(f"Calculated legal moves: {squares=}")
        return squares


class Move:
    def __init__(self, from_square, to_square):
        self.from_square = from_square
        self.to_square = to_square

    def __str__(self):
        return f"{self.from_square} to {self.to_square}"
