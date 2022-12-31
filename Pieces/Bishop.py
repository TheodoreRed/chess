try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Bishop(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)

    def move(self, board, new_pos):
        return True

    def __repr__(self):
        return "B " + str(self.team)
