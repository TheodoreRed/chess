try:
    from Pieces.Piece import *
except:
    from Piece import *


class King(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.KING

    """
    def get_legal_moves(self, board, position):
        legal_moves = []
        row, col = position[0], position[1]

        for i in range(3):
            test_row = (row + i) - 1
            for j in range(3):
                test_col = (col + j) - 1
                if (test_col >= 0 and test_row >= 0) and (
                    test_col <= 7 and test_row <= 7
                ):
                    if board[test_row][test_col]:
                        piece = board[test_row][test_col]
                        if piece.team != self.team:
                            legal_moves.append((test_row, test_col))
                    else:
                        legal_moves.append((test_row, test_col))
        return legal_moves
    """

    def move(self, board, current_pos, new_pos, testing=False):
        new_row, new_col = new_pos[0], new_pos[1]
        current_row, current_col = current_pos[0], current_pos[1]

        # King can only move one
        if abs(current_row - new_row) > 1 or abs(current_col - new_col) > 1:
            not testing and print("Try again: Kings can only move one space at a time.")
            return False

        # Attacking
        if board[new_row][new_col] != None:
            if board[new_row][new_col].team == self.team:
                not testing and print("Try again: Your own piece is blocking the way.")
                return False

        return True
