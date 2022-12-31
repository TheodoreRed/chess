try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Rook(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)

    def move(self, board, current_pos, new_pos):
        # Vertical Change
        if new_pos[1] == current_pos[1]:

            # Up or Down
            route = 1 if new_pos[0] > current_pos[0] else -1
            for i in range(current_pos[0] + route, new_pos[0] + route, route):
                if board[i][new_pos[1]] != None:
                    if board[i][new_pos[1]].team is self.team:
                        print("Same team!")
                        return False
                    if i != new_pos[0]:
                        print("Piece in the way")
                        return False
                    return True
            return True

        # Horizontal Change
        if new_pos[0] == current_pos[0]:
            # Up or Down
            route = 1 if new_pos[1] > current_pos[1] else -1
            for i in range(current_pos[1] + route, new_pos[1] + route, route):
                if board[new_pos[0]][i] != None:
                    if board[new_pos[0]][i].team is self.team:
                        print("Same Team!")
                        return False
                    else:
                        if i != new_pos[1]:
                            print("Piece in the way")
                            return False
                    return True
            return True

        print("Not same row or column")
        return False

    def __repr__(self):
        return "R " + str(self.team)
