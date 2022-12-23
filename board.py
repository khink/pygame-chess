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
