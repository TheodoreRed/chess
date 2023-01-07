try:
    from Pieces.Piece import *
except:
    from Piece import *


class Bishop(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.BISHOP

    def move(self, board, current_pos, new_pos):
        new_row, new_col = new_pos
        current_row, current_col = current_pos
        
        row_diff = abs(new_row - current_row)
        col_diff = abs(new_col - current_col)

        # Checks if new_pos is a diagonal
        if row_diff == col_diff:

            row_route = 1 if new_row > current_row else -1
            col_route = 1 if new_col > current_col else -1
            for i in range(1, row_diff + 1):
                row_increment = row_route * i
                col_increment = col_route * i
                if board[current_row + row_increment][current_col + col_increment]:
                    if board[current_row + row_increment][current_col + col_increment].get_team() == self.get_team():
                        print("Try again: Your own piece is blocking the way.")
                        return False
            return True

        print("Try again: Bishops can only move in a diagonal.")
        return False
