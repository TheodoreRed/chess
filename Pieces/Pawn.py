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

        # moving vertically
        if new_col == current_col:
            moves_allowed = 2 if self.first_move == True else 1
            if abs(new_row - current_row) <= moves_allowed:
                if board[new_row][new_col] != None:
                    print("Piece in the way")
                    return False
                self.first_move = False
                return True
        # trying to attack
        if abs(current_row - new_row) == 1 and abs(current_col - new_col) == 1:
            route = 1 if new_row > current_row else -1
            if str(self.team) == "Team.WHITE":
                if route != 1:
                    return False
            else:
                if route != -1:
                    return False

            return True

        print("Can't move there!")
        return False

    def __repr__(self):
        return "P " + str(self.team)
