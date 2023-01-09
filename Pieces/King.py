try:
    from Pieces.Piece import *
except:
    from Piece import *


class King(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.KING

    def move(self, board, current_pos, new_pos, testing=False):
        new_row, new_col = new_pos
        current_row, current_col = current_pos
        
        row_diff, col_diff = abs(current_row - new_row), abs(current_col - new_col)

        # King can only move one
        if row_diff > 1 or col_diff > 1:
            not testing and print("Try again: Kings can only move one space at a time.")
            return False

        # Attacking
        if board[new_row][new_col]:
            if board[new_row][new_col].get_team() == self.get_team():
                not testing and print("Try again: Your own piece is blocking the way.")
                return False

        return True
