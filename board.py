class Board:
    """Keeps track where pieces are, and which moves are valid.

    Chess stuff only! Rendering / input goes in BoardScreen.
    """

    def __init__(self, ranks, files):
        self.ranks = ranks
        self.files = files

        # TODO load initial setup from PGN or something
        self.squares = [
            "r",
            "n",
            "b",
            "k",
            "q",
            "p",
            "p",
            "p",
            "p",
            "p",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            "P",
            "P",
            "P",
            "P",
            "P",
            "R",
            "N",
            "B",
            "K",
            "Q",
        ]

    def get_valid_moves(self, board_rank, board_file):
        index = board_rank * self.files + board_file
        piece_code = self.squares[index]

        # TODO add all other pieces, take board boundaries into account
        if piece_code == "P":
            return [(board_rank - 1, board_file)]

        return []
