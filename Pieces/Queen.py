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

    def get_legal_moves(self, board, position):
        legal_moves = []
        bishop = Bishop(self.team)
        for move in bishop.get_legal_moves(board, (position[0], position[1])):
            legal_moves.append(move)
        rook = Rook(self.team)
        for move in rook.get_legal_moves(board, (position[0], position[1])):
            legal_moves.append(move)
        return legal_moves

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
