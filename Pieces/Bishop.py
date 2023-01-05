try:
    from Pieces.Piece import *
except:
    from Piece import *


class Bishop(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.BISHOP

    def get_legal_moves(self, board, position):
        legal_moves = []
        row, col = position[0], position[1]
        up_right, up_left, down_right, down_left = True, True, True, True

        for i in range(1, len(board) + 1):
            if row + i <= 7 and col + i <= 7:
                if up_right:
                    if board[row + i][col + i] == None:
                        legal_moves.append((row + i, col + i))
                    else:
                        if board[row + i][col + i].team != self.team:
                            legal_moves.append((row + i, col + i))
                        up_right = False
            if row + i <= 7 and col - i >= 0:
                if up_left:
                    if board[row + i][col - i] == None:
                        legal_moves.append((row + i, col - i))
                    else:
                        if board[row + i][col - i].team != self.team:
                            legal_moves.append((row + i, col - i))
                        up_left = False
            if row - i >= 0 and col - i >= 0:
                if down_left:
                    if board[row - i][col - i] == None:
                        legal_moves.append((row - i, col - i))
                    else:
                        if board[row - i][col - i].team != self.team:
                            legal_moves.append((row - i, col - i))
                        down_left = False
            if row - i >= 0 and col - i >= 0:
                if down_right:
                    if board[row - i][col + i] == None:
                        legal_moves.append((row - i, col + i))
                    else:
                        if board[row - i][col + i].team != self.team:
                            legal_moves.append((row - i, col + i))
                        down_right = False
        return legal_moves

    def move(self, board, current_pos, new_pos):
        new_row, new_col = new_pos[0], new_pos[1]
        current_row, current_col = current_pos[0], current_pos[1]

        # Checks if new_pos is a diagonal
        if abs(new_row - current_row) == abs(new_col - current_col):

            row_route = 1 if new_row > current_row else -1
            col_route = 1 if new_col > current_col else -1
            for i in range(1, abs(new_row - current_row) + 1):
                row_increment = row_route * i
                col_increment = col_route * i
                if (
                    board[current_row + row_increment][current_col + col_increment]
                    != None
                ):
                    if (
                        board[current_row + row_increment][
                            current_col + col_increment
                        ].team
                        == self.team
                    ):
                        print("Try again: Your own piece is blocking the way.")
                        return False
                    else:
                        return True
            return True
        print("Try again: Bishops can only move in a diagonal.")
        return False
