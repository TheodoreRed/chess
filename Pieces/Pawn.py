try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Pawn(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.first_move = True

    def move(self, board, current_pos, new_pos):
        new_row = new_pos[0]
        new_col = new_pos[1]
        current_row = current_pos[0]
        current_col = current_pos[1]

        if new_col == current_col:
            moves_allowed = 2 if self.first_move == True else 1
            if abs(new_row - current_row) <= moves_allowed:
                self.first_move = False
                return True

        print("Can't move there!")
        return False

    def __repr__(self):
        return "P " + str(self.team)
