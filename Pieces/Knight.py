try:
    from Pieces.Piece import *
except:
    from Piece import *


class Knight(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.KNIGHT

    def move(self, board, current_pos, new_pos):
        return True
