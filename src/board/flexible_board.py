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

    def get_valid_moves(self, board_rank, board_file):
        index = board_rank * self.files + board_file
        piece_code = self.squares[index]

        # TODO add all other pieces, take board boundaries into account
        if piece_code == "P":
            return [(board_rank - 1, board_file)]

        return []
