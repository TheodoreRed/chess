try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Knight(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.first_move = True

    def move(self, board, current_pos, new_pos):
        return True

    def __repr__(self):
        return "K " + str(self.team)
