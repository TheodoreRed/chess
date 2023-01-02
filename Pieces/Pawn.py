try:
    from Pieces.Piece import *
except:
    from Piece import *


class Pawn(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.PAWN
        
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
                """
                TODO: This is missing some logic I think.

                what if you move a pawn from a2 to a4, but there's a piece at a3 blocking your way? This doesn't check for that case
                """
                if board[new_row][new_col] != None:
                    print("Piece in the way")
                    return False
                self.first_move = False
                if new_row > current_row and self.is_white_team():
                    return True
                elif new_row < current_row and not self.is_white_team():
                    return True
        # trying to attack
        # TODO: you could define "row_diff" and "col_diff" at the top of the method and it'd be easier to read I think
        elif abs(current_row - new_row) == 1 and abs(current_col - new_col) == 1:
            if board[new_row][new_col] != None:
                if board[new_row][new_col].team != self.team:
                    if new_row > current_row and self.is_white_team():
                        return True
                    elif new_row < current_row and not self.is_white_team():
                        return True

        print("Can't move there!")
        return False
