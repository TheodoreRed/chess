try:
    from Pieces.Piece import *
except:
    from Piece import *


class Rook(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.ROOK

    def move(self, board, current_pos, new_pos, testing=False):
        new_row, new_col = new_pos
        current_row, current_col = current_pos

        # Vertical Change
        if new_col == current_col:
            # Up or Down
            route = 1 if new_row > current_row else -1
            for i in range(current_row + route, new_row + route, route):
                if board[i][new_col]:
                    if board[i][new_col].get_team() is self.get_team():
                        not testing and print("Try again: Your own piece is blocking the way.")
                        return False
                    elif i != new_row:
                        not testing and print("Try again: There is an enemy piece blocking your way.")
                        return False
            return True

        # Horizontal Change
        if new_row == current_row:
            # Left or Right
            route = 1 if new_col > current_col else -1
            for i in range(current_col + route, new_col + route, route):
                if board[new_row][i]:
                    if board[new_row][i].get_team() is self.get_team():
                        not testing and print("Try again: Your own piece is blocking the way.")
                        return False
                    else:
                        if i != new_col:
                            not testing and print("Try again: There is an enemy piece blocking your way.")
                            return False
            return True

        not testing and print("Try again: Rooks can only move along ranks and files, not diagonals.")
        return False
