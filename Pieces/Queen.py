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

    def move(self, board, current_pos, new_pos):

        """
        Most importantly, you don't have to update this code everytime you update Rook/Bishop... D. R. Y. !!!
        """
        bishop = Bishop(self.team)
        rook = Rook(self.team)
        if bishop.move(board, current_pos, new_pos) or rook.move(
            board, current_pos, new_pos
        ):
            return True
        else:
            print("Try again: Queens can only move along straight lines and diagonals.")
            return False
