from Pieces.Piece import Team
from Pieces.Rook import Rook


class Board:
    def __init__(self):
        BOARD_SIZE = 8
        self.board = [[0] * BOARD_SIZE] * BOARD_SIZE
        self.populate_board()

    def populate_board(self):
        i = 0
        while i < 2:
            row = self.board[i]
            for j in range(len(row)):
                # row[j] = Rook(Team.WHITE, (i, j))
                row[j] = 1
                print(j)
            i += 1

    def display(self):
        for row in self.board:
            print(row)


board = Board()
board.display()
