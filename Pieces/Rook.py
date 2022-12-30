try:
    from Pieces.Piece import Piece
except:
    from Piece import Piece


class Rook(Piece):
    def __init__(self, team, position):
        Piece.__init__(self, team, position)

    # TODO: Check legality,
    def move(self, board, new_pos):
        # checks if new_pos in same row or column
        if new_pos[0] == self.position[0] or new_pos[1] == self.position[1]:

            # checks if new position is changing vertically
            if new_pos[1] == self.position[1]:

                # increasing
                if new_pos[0] > self.position[0]:
                    for i in range(self.position[0] + 1, new_pos[0] + 1):
                        if board[i][new_pos[1]] != None:
                            if board[i][new_pos[1]].team is not self.team:
                                if i != new_pos[0]:
                                    print(i, new_pos[1])
                                    print("Piece in the way")
                                    return False
                                self.position = new_pos
                                return True
                            print("Same team!")
                            return False
                    self.position = new_pos
                    return True

                # decreasing
                else:
                    for i in range(self.position[0] - 1, new_pos[0] - 1, -1):
                        if board[i][new_pos[1]] != None:
                            if board[i][new_pos[1]].team is self.team:
                                print("Same Team!")
                                return False
                            else:
                                if i != new_pos[0]:
                                    print("Piece in the way")
                                    return False
                    self.position = new_pos
                    return True
            # checks if new position is changing horizontally
            else:
                if new_pos[0] == self.position[0]:
                    # increasing
                    if new_pos[1] > self.position[1]:
                        for i in range(self.position[1] + 1, new_pos[1] + 1):
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
                    # decreasing
                    else:
                        for i in range(self.position[1] - 1, new_pos[1] - 1, -1):
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

        else:
            print("Not same row or column")
            return False

    def __str__(self):
        return "R" + str(self.team)
