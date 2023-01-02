try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class King(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.first_move = True

    def move(self, board, current_pos, new_pos):
        new_row = new_pos[0]
        new_col = new_pos[1]
        current_row = current_pos[0]
        current_col = current_pos[1]

        # King can only move one
        if abs(current_row - new_row) > 1 or abs(current_col - new_col) > 1:
            print("Can't move there!")
            return False

        # Checks if new position will be near enemy king
        for i in range(3):
            test_row = (new_row + i) - 1
            for j in range(3):
                test_col = (new_col + j) - 1
                if (test_col >= 0 and test_row >= 0) and (
                    test_col <= 7 and test_row <= 7
                ):
                    if board[test_row][test_col] != None:
                        # Unorthodox way of checking if its of type King
                        if (
                            str(type(board[test_row][test_col]))
                            == "<class 'Pieces.King.King'>"
                            # I wont need this 'and' after poulate board() is correct becasue theres only one other king
                        ) and board[test_row][test_col].team != self.team:
                            print("Can't move near enemy king")
                            return False
        # Attacking
        if board[new_row][new_col] != None:
            if board[new_row][new_col].team == self.team:
                print("Same team")
                return False
        return True

    def __repr__(self):
        return "King " + str(self.team)
