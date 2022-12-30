from Pieces.Piece import Team
from Pieces.Rook import Rook

BOARD_SIZE = 8


class Board:
    def __init__(self):
        self.board = []
        self.populate_board()

    def populate_board(self):
        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                if i in {0, 1, 6, 7}:
                    team = Team.WHITE if i in {0, 1} else Team.BLACK
                    row.append(Rook(team, (i, j)))
                else:
                    row.append(None)
            self.board.append(row)

    def display(self):
        print("---------------------------")
        for row in self.board:
            print(row)

    def move(self, current_pos, new_pos):
        piece = self.board[current_pos[0]][current_pos[1]]
        if piece:
            if piece.move(self.board, new_pos):
                self.board[current_pos[0]][current_pos[1]] = None
                self.board[new_pos[0]][new_pos[1]] = piece
        else:
            print("No Piece Exists")


board = Board()
board.display()
board.move((1, 0), (5, 0))
board.display()
print("----------------------")
