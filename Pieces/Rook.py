try:
    from Pieces.Piece import *
except:
    from Piece import *


class Rook(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.ROOK

    def get_legal_moves(self, board, position):
        legal_moves = []
        row, col = position[0], position[1]
        move_left, move_right, move_up, move_down = True, True, True, True

        for i in range(1, len(board) + 1):
            if col - i >= 0:
                if move_left:
                    if board[row][col - i] == None:
                        legal_moves.append((row, col - i))
                    else:
                        if board[row][col - i].team != self.team:
                            legal_moves.append((row, col - i))
                        move_left = False
            if col + i <= 7:
                if move_right:
                    if board[row][col + i] == None:
                        legal_moves.append((row, col + i))
                    else:
                        if board[row][col + i].team != self.team:
                            legal_moves.append((row, col + i))
                        move_right = False
            if row + i <= 7:
                if move_up:
                    if board[row + i][col] == None:
                        legal_moves.append((row + i, col))
                    else:
                        if board[row + i][col].team != self.team:
                            legal_moves.append((row + i, col))
                        move_up = False
            if row - i >= 0:
                if move_down:
                    if board[row - i][col] == None:
                        legal_moves.append((row - i, col))
                    else:
                        if board[row - i][col].team != self.team:
                            legal_moves.append((row - i, col))
                        move_down = False
        print(legal_moves)
        return legal_moves

    def move(self, board, current_pos, new_pos):
        new_row, new_col = new_pos[0], new_pos[1]
        current_row, current_col = current_pos[0], current_pos[1]

        # Vertical Change
        if new_col == current_col:
            # Up or Down
            route = 1 if new_row > current_row else -1
            for i in range(current_row + route, new_row + route, route):
                if board[i][new_col] != None:
                    if board[i][new_col].team is self.team:
                        print("Try again: Your own piece is blocking the way.")
                        return False
                    elif i != new_row:
                        print("Try again: There is an enemy piece blocking your way.")
                        return False
            return True

        # Horizontal Change
        if new_row == current_row:
            # Left or Right
            route = 1 if new_col > current_col else -1
            for i in range(current_col + route, new_col + route, route):
                if board[new_row][i] != None:
                    if board[new_row][i].team is self.team:
                        print("Try again: Your own piece is blocking the way.")
                        return False
                    else:
                        if i != new_col:
                            print(
                                "Try again: There is an enemy piece blocking your way."
                            )
                            return False
                    return True
            return True

        print("Try again: Rooks can only move along ranks and files, not diagonals.")
        return False
