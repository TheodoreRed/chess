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
        # horizontal move
        if new_pos[0] == self.position[0]:
            return True
        # vertical move
        elif new_pos[1] == self.position[1]:
            VERTICAL = new_pos[1]

            # new position is increasing
            if self.position[0] < new_pos[0]:
                print("Increasing vertical")
                for i in range((self.position[0] + 1), (new_pos[0] + 1)):
                    print(i)
                    # checks if there is a piece
                    if board[i][VERTICAL] != None:
                        if board[i][VERTICAL].team != self.team:
                            print("XXXXxxxXX")
                            self.position = (new_pos[0] - 1, new_pos[1])
                            return True
                        return False
                self.position = new_pos
                return True
            # new position decreasing
            else:
                print("Decreasing")
                """
                for i in range(new_pos[0], self.position[0] + 1):
                    if board[i][VERTICAL] != None:
                        # spot not empty
                        print("Can't move there!")
                        return False
                """
                return True
        else:
            return False

    def __str__(self):
        return "R" + self.team
