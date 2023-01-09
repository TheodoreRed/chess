try:
    from Pieces.Piece import *
    from Pieces.Bishop import *
    from Pieces.Rook import *
except:
    from Piece import *


class Queen(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.QUEEN
        
    def move(self, board, current_pos, new_pos, testing=False):
        bishop = Bishop(self.team)
        rook = Rook(self.team)

        if bishop.move(board, current_pos, new_pos, True) or rook.move(board, current_pos, new_pos, True):
            return True
        else:
            not testing and print("Try again: Queens can only move along straight lines and diagonals.")
            return False
