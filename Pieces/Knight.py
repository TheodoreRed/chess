try:
    from Pieces.Piece import *
except:
    from Piece import *


class Knight(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.KNIGHT

    def get_legal_moves(self, board, position):
        legal_moves = []
        row, col = position[0], position[1]
        return legal_moves

    def move(self, board, current_pos, new_pos):
        return True
