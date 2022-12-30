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

        if new_pos[0] == self.position[0]:
            # horizontal move
            print("horizontal")
            return True
        elif new_pos[1] == self.position[1]:
            vertical = new_pos[1]
            # vertical move
            if self.position[0] < new_pos[0]:
                for i in range(self.position[0] + 1, new_pos[0] + 1):
                    if board[i][vertical] != None:
                        # spot not empty
                        print("Can't move there!")
                        return False
                return True
        else:
            return False

    def __str__(self):
        return "R"
