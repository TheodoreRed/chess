try:
    from Pieces.Piece import *
except:
    from Piece import *


class Pawn(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.PAWN

    # TODO: fix this method
    def get_legal_moves(self, board, position):
        legal_moves = []
        row, col = position[0], position[1]
        if self.team == Team.WHITE and row + 1 <= 7:
            if board[row + 1][col] == None:
                legal_moves.append((row + 1, col))
                if self.first_move and row + 2 <= 7:
                    if board[row + 2][col] == None:
                        legal_moves.append((row + 2, col))
            if col + 1 <= 7:
                if board[row + 1][col + 1]:
                    if board[row + 1][col + 1].team != self.team:
                        legal_moves.append((row + 1, col + 1))
            if col - 1 >= 0:
                if board[row + 1][col - 1]:
                    if board[row + 1][col - 1].team != self.team:
                        legal_moves.append((row + 1, col - 1))

        # black pawns go down
        if self.team == Team.BLACK and row - 1 >= 0:
            if board[row - 1][col] == None:
                legal_moves.append((row - 1, col))
                if self.first_move and row - 2 >= 0:
                    if board[row - 2][col] == None:
                        legal_moves.append((row - 2, col))
            if col - 1 >= 0:
                if board[row - 1][col - 1]:
                    if board[row - 1][col - 1].team != self.team:
                        legal_moves.append((row - 1, col - 1))
            if col + 1 <= 7:
                if board[row - 1][col + 1]:
                    if board[row - 1][col + 1].team != self.team:
                        legal_moves.append((row - 1, col + 1))
        return legal_moves

    def move(self, board, current_pos, new_pos):
        new_row, new_col = new_pos[0], new_pos[1]
        current_row, current_col = current_pos[0], current_pos[1]
        row_diff = abs(current_row - new_row)
        col_diff = abs(current_col - new_col)

        # moving vertically
        if new_col == current_col:
            moves_allowed = 2 if self.first_move == True else 1
            if row_diff <= moves_allowed:
                route = 1 if new_row > current_row else -1
                if (
                    board[new_row][new_col] != None
                    or board[current_row + route][current_col]
                ):
                    print("Try again: There is another piece blocking it's path.")
                    return False

                if new_row > current_row and self.is_white_team():
                    return True
                elif new_row < current_row and not self.is_white_team():
                    return True
        # trying to attack
        elif row_diff == 1 and col_diff == 1:
            if board[new_row][new_col] != None:
                if board[new_row][new_col].team != self.team:
                    if new_row > current_row and self.is_white_team():
                        return True
                    elif new_row < current_row and not self.is_white_team():
                        return True

        print(
            "Try again: Pawns can only move two squares on their first move, and one square on all other moves. Move diagonal to attack."
        )
        return False
