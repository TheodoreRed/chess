try:
    from Pieces.Piece import *
except:
    from Piece import *


class Pawn(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.PAWN

    def move(self, board, current_pos, new_pos, testing=False):
        new_row, new_col = new_pos
        current_row, current_col = current_pos

        row_diff = abs(current_row - new_row)
        col_diff = abs(current_col - new_col)

        # moving vertically
        if new_col == current_col:
            moves_allowed = 2 if self.first_move == True else 1
            if row_diff <= moves_allowed:
                route = 1 if new_row > current_row else -1
                if (board[new_row][new_col] or board[current_row + route][current_col]):
                    not testing and print("Try again: Your own piece is blocking the way.")
                    return False

                if new_row > current_row and self.is_white_team():
                    return True
                elif new_row < current_row and not self.is_white_team():
                    return True
        # trying to attack
        elif row_diff == 1 and col_diff == 1:
            if board[new_row][new_col]:
                if board[new_row][new_col].get_team() != self.get_team():
                    if new_row > current_row and self.is_white_team():
                        return True
                    elif new_row < current_row and not self.is_white_team():
                        return True

        not testing and print("Try again: Pawns can only move two squares on their first move, and one square on all other moves. Move diagonal to attack.")
        return False
