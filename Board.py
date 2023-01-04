import os
from copy import deepcopy

from Pieces.Piece import Team, Rank
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Knight import Knight

os.system("cls")


BOARD_SIZE = 8
DEFAULT_BOARD = [
    [
        Rook(Team.WHITE),
        Knight(Team.WHITE),
        Bishop(Team.WHITE),
        Queen(Team.WHITE),
        King(Team.WHITE),
        Bishop(Team.WHITE),
        Knight(Team.WHITE),
        Rook(Team.WHITE),
    ],
    [
        Pawn(Team.WHITE),
        Pawn(Team.WHITE),
        Pawn(Team.WHITE),
        Pawn(Team.WHITE),
        Pawn(Team.WHITE),
        Pawn(Team.WHITE),
        Pawn(Team.WHITE),
        Pawn(Team.WHITE),
    ],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [
        Pawn(Team.BLACK),
        Pawn(Team.BLACK),
        Pawn(Team.BLACK),
        Pawn(Team.BLACK),
        Pawn(Team.BLACK),
        Pawn(Team.BLACK),
        Pawn(Team.BLACK),
        Pawn(Team.BLACK),
    ],
    [
        Rook(Team.BLACK),
        Knight(Team.BLACK),
        Bishop(Team.BLACK),
        Queen(Team.BLACK),
        King(Team.BLACK),
        Bishop(Team.BLACK),
        Knight(Team.BLACK),
        Rook(Team.BLACK),
    ],
]


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

    # check if a team is in check
    def in_check(self, team):
        king = None
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] != None:
                    piece = self.board[row][col]
                    if piece.rank == Rank.KING and piece.team == team:
                        king_row = row
                        king_col = col
                        king = piece
                        break
        # This will eventually be legal moves of a queen and Knight
        rook = Rook(team)
        potential_enemies = rook.get_legal_moves(self.board, (king_row, king_col))
        enemies = []
        for position in potential_enemies:
            row, col = position[0], position[1]
            print(row, col)
            print(self.board[row][col])
        return False

    def move(self, current_pos, new_pos):
        piece = self.get_piece(current_pos)
        if piece:
            """
            TODO: (for me) change how we get a reference to board inside of each piece instance. It will be better (and cleaner)
            to have a reference to the board object instead of the board array in each piece. This will be a big re-factor, so I'm
            holding off on it for now
            """
            if piece.move(self.board, current_pos, new_pos):
                if self.in_check(piece.team) == False:
                    self.board[current_pos[0]][current_pos[1]] = None
                    self.board[new_pos[0]][new_pos[1]] = piece

                self.display()

                return True

    # TODO: return team of winner, or None if the game needs to continue
    def is_game_over(self):
        # if self.in_check(Team.WHITE) and
        # if self.can_not_move_piece_to_check_lane(Team.WHITE)
        # if self.can_not_move_king(Team.WHITE)
        return None


board = Board()
board.move((1, 4), (3, 4))
board.move((6, 0), (4, 0))
board.move((7, 0), (5, 0))
board.move((5, 0), (5, 3))
board.move((5, 3), (2, 3))
board.move((2, 3), (2, 4))

"""
rook = board.board[2][1]
print(rook)
rook.get_legal_moves(board.board, (2, 1))
"""
