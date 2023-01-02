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

        # Checks if new_pos is a diagonal
        if abs(new_row - current_row) == abs(new_col - current_col):

            row_route = 1 if new_row > current_row else -1
            col_route = 1 if new_col > current_col else -1
            for i in range(abs(new_row - current_row)):
                if board[current_row + row_route][current_col + col_route] != None:
                    if (
                        board[current_row + row_route][current_col + col_route].team
                        == self.team
                    ):
                        print("Same Team!")
                        return False
                    else:
                        return True
                current_row += row_route
                current_col += col_route
            return True
        print("Can't move there!")
        return False

    def __repr__(self):
        return "B " + str(self.team)
