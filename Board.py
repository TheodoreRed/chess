from Pieces.Piece import Team
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
import os

os.system("cls")


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
                    row.append(Pawn(team))
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
            if piece.move(self.board, current_pos, new_pos):
                self.board[current_pos[0]][current_pos[1]] = None
                self.board[new_pos[0]][new_pos[1]] = piece
        else:
            print("No Piece Exists")


board = Board()
board.display()

board.move((6, 0), (4, 0))
board.display()
board.move((4, 0), (3, 0))
board.display()
board.move((3, 0), (2, 0))
board.display()
board.move((2, 0), (1, 1))
board.display()
board.move((1, 1), (0, 0))
board.display()


print("----------------------")
