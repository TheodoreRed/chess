from Pieces.Piece import Team
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Knight import Knight
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
                if i in {1, 6}:
                    team = Team.WHITE if i == 1 else Team.BLACK
                    row.append(Pawn(team))
                elif i in {0, 7}:
                    team = Team.WHITE if i == 0 else Team.BLACK
                    if j in {0, 7}:
                        row.append(Rook(team))
                    elif j in {1, 6}:
                        row.append(Knight(team))
                    elif j in {2, 5}:
                        row.append(Bishop(team))
                    elif j == 3:
                        row.append(Queen(team))
                    elif j == 4:
                        row.append(King(team))
                    else:
                        row.append(None)
                else:
                    row.append(None)
            self.board.append(row)

    def display(self):
        print("---------------------------")
        for row in reversed(range(len(self.board))):
            print(self.board[row])

    # Gets every legal move given a spot on the board
    # TODO: Prints error messages for move and turns
    # off `first_move` for any piece that needs it
    def get_all_legal_moves(self, position):
        legal_moves = []
        if self.board[position[0]][position[1]] != None:
            piece = self.board[position[0]][position[1]]
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if piece.move(self.board, (position[0], position[1]), (row, col)):
                        legal_moves.append((row, col))
        return legal_moves

    def move(self, current_pos, new_pos):
        piece = self.board[current_pos[0]][current_pos[1]]
        if piece:
            if piece.move(self.board, current_pos, new_pos):
                self.board[current_pos[0]][current_pos[1]] = None
                self.board[new_pos[0]][new_pos[1]] = piece
        else:
            print("No Piece Exists")


board = Board()
board.move((1, 0), (3, 0))
board.display()
board.move((3, 0), (2, 0))
board.display()
print(board.get_all_legal_moves((3, 0)))
print("----------------------")
