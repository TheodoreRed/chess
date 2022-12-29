from Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, team, position):
        Piece.__init__(self, team, position)

    # TODO: Check legality,
    def move(self, board, new_pos):
        return True

    def __str__(self):
        return "R"
