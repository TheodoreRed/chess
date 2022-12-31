try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Rook(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)

    def move(self, board, current_pos, new_pos):
        new_row = new_pos[0]
        new_col = new_pos[1]
        current_row = current_pos[0]
        current_col = current_pos[1]

        # Vertical Change
        if new_col == current_col:

            # Up or Down
            route = 1 if new_row > current_row else -1
            for i in range(current_row + route, new_row + route, route):
                if board[i][new_col] != None:
                    if board[i][new_col].team is self.team:
                        print("Same team!")
                        return False
                    if i != new_row:
                        print("Piece in the way")
                        return False
                    return True
            return True

        # Horizontal Change
        if new_row == current_row:

            # Up or Down
            route = 1 if new_col > current_col else -1
            for i in range(current_col + route, new_col + route, route):
                if board[new_row][i] != None:
                    if board[new_row][i].team is self.team:
                        print("Same Team!")
                        return False
                    else:
                        if i != new_col:
                            print("Piece in the way")
                            return False
                    return True
            return True

        print("Not same row or column")
        return False

    def __repr__(self):
        return "R " + str(self.team)
