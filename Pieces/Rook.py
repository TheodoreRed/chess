try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Rook(Piece):
    def __init__(self, team, position):
        Piece.__init__(self, team, position)

    def move(self, board, new_pos):
        # Vertical Change
        if new_pos[1] == self.position[1]:

            # Up or Down
            route = 1 if new_pos[0] > self.position[0] else -1
            for i in range(self.position[0] + route, new_pos[0] + route, route):
                if board[i][new_pos[1]] != None:
                    if board[i][new_pos[1]].team is self.team:
                        print("Same team!")
                        print(route)
                        return False
                    if i != new_pos[0]:
                        print("Piece in the way")
                        return False
                    self.position = new_pos
                    return True
            self.position = new_pos
            return True

        # Horizontal Change
        if new_pos[0] == self.position[0]:
            # Up or Down
            route = 1 if new_pos[1] > self.position[1] else -1
            for i in range(self.position[1] + route, new_pos[1] + route, route):
                if board[new_pos[0]][i] != None:
                    if board[new_pos[0]][i].team is self.team:
                        print("Same Team!")
                        return False
                    else:
                        if i != new_pos[1]:
                            print("Piece in the way")
                            return False
            self.position = new_pos
            return True

        print("Not same row or column")
        return False

    def __repr__(self):
        team = "Black" if str(self.team).__contains__("BLACK") else "White"

        return "R " + team
