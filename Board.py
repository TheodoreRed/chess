import os
from copy import deepcopy

from Pieces.Piece import Team
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Knight import Knight

os.system("cls")


BOARD_SIZE = 8
DEFAULT_BOARD = [[Rook(Team.WHITE), Knight(Team.WHITE), Bishop(Team.WHITE), Queen(Team.WHITE), King(Team.WHITE), Bishop(Team.WHITE), Knight(Team.WHITE), Rook(Team.WHITE)],
                 [Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE)],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK)],
                 [Rook(Team.BLACK), Knight(Team.BLACK), Bishop(Team.BLACK), Queen(Team.BLACK), King(Team.BLACK), Bishop(Team.BLACK), Knight(Team.BLACK), Rook(Team.BLACK)]]


class Board:
    def __init__(self, starting_board=DEFAULT_BOARD):
        self.board = []
        self.populate_board(starting_board)

    def populate_board(self, starting_board):
        self.board = deepcopy(starting_board)

    def display(self):
        print("---------------------------")
        for row in reversed(range(len(self.board))):
            print(self.board[row])
    
    def get_board(self):
        return self.board
    
    def get_piece(self, pos):
        piece = self.board[pos[0]][pos[1]]
        if piece:
            return piece

    # Gets every legal move given a spot on the board
    # TODO: Prints error messages for move and turns
    # off `first_move` for any piece that needs it

    # note: careful with how you use this method... it is extremely expensive (I'm sure you know that but still be cautious)
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
        piece = self.get_piece(current_pos)
        if piece:
            """
            TODO: (for me) change how we get a reference to board inside of each piece instance. It will be better (and cleaner)
            to have a reference to the board object instead of the board array in each piece. This will be a big re-factor, so I'm
            holding off on it for now
            """
            if piece.move(self.board, current_pos, new_pos):
                self.board[current_pos[0]][current_pos[1]] = None
                self.board[new_pos[0]][new_pos[1]] = piece

                self.display()

                return True
    
    # TODO: return team of winner, or None if the game needs to continue
    def is_game_over(self):
        return None


"""
board = Board()
board.move((1, 0), (3, 0))
board.display()
board.move((3, 0), (2, 0))
board.display()
print(board.get_all_legal_moves((3, 0)))
print("----------------------")
"""
