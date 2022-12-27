from Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, team, position):
        Piece.__init__(self, team, position)

    def move(self, board, new_pos):
        pass
