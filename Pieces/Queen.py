try:
    from Pieces.Piece import *
except:
    from Piece import *


class Queen(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.QUEEN

    def move(self, board, current_pos, new_pos):
        """
        TODO: Instead of copying this... could you just use the Rook and Bishop directly? Why not make new Rook/Bishop objects...
        test them to see if *they* would move successfully then you know that the queen could as well.

        Most importantly, you don't have to update this code everytime you update Rook/Bishop... D. R. Y. !!!
        """
        new_row = new_pos[0]
        new_col = new_pos[1]
        current_row = current_pos[0]
        current_col = current_pos[1]

        # Checks if new_pos is a diagonal
        if abs(new_row - current_row) == abs(new_col - current_col):

            row_route = 1 if new_row > current_row else -1
            col_route = 1 if new_col > current_col else -1
            for i in range(abs(new_row - current_row)):
                if board[current_row + row_route][current_col + col_route] != None:
                    if (
                        board[current_row + row_route][current_col + col_route].team
                        == self.team
                    ):
                        print("Same Team!")
                        return False
                    else:
                        return True
                current_row += row_route
                current_col += col_route
            return True
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
        print("Can't move there!")
        return False
