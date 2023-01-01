try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Bishop(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)

    def move(self, board, current_pos, new_pos):
        new_row = new_pos[0]
        new_col = new_pos[1]
        current_row = current_pos[0]
        current_col = current_pos[1]
        if abs(new_row - current_row) == abs(new_col - current_col):
            return True
        print("Not a diagonal")
        return False

    def __repr__(self):
        return "B " + str(self.team)
