try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Pawn(Piece):
    def __init__(self, team, position):
        Piece.__init__(self, team, position)

    def move(self, board, new_pos):
        return True

    def __repr__(self):
        team = "Black" if str(self.team).__contains__("BLACK") else "White"

        return "P " + team
