try:
    from Pieces.Piece import *
except:
    from Piece import *


class Knight(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.KNIGHT

    def move(self, board, current_pos, new_pos):
        new_row, new_col = new_pos
        current_row, current_col = current_pos

        row_diff = abs(current_row - new_row)
        col_diff = abs(current_col - new_col)

        # knights only ever have 8 potential moves, all of which follow one of these two patterns
        if (row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1):
            piece = board[new_row][new_col]
            if piece and piece.team == self.team:
                print("Try again: Your own piece is blocking the way.")
                return False
            
            # knights can skip over pieces, so the only thing ever preventing a knight from moving is their own team's piece being in the way
            return True
