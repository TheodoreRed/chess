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

    # trys all the legal moves on a team. if it finds one that stops check returns true
    def try_all_legal_moves(self, team):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] != None:
                    piece = self.board[row][col]
                    if piece.team == team:
                        piece_moves = piece.get_legal_moves(self.board, (row, col))
                        for move in piece_moves:
                            if piece.move(self.board, (row, col), (move[0], move[1])):
                                self.board[row][col] = None
                                self.board[move[0]][move[1]] = piece
                                if self.in_check(piece.team) == False:
                                    self.board[row][col] = piece
                                    self.board[move[0]][move[1]] = None
                                    # found a spot that would get out of check
                                    return True
                                else:
                                    self.board[row][col] = piece
                                    self.board[move[0]][move[1]] = None
        return False

    def get_kings_position(self, team):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] != None:
                    piece = self.board[row][col]
                    if piece.rank == Rank.KING and piece.team == team:
                        return (row, col)

    # check if a team is in check
    def in_check(self, team):
        king_pos = self.get_kings_position(team)
        king_row = king_pos[0]
        king_col = king_pos[1]
        # This will eventually be legal moves of a queen and Knight
        rook = Rook(team)
        potential_enemies = rook.get_legal_moves(self.board, (king_row, king_col))
        for position in potential_enemies:
            row, col = position[0], position[1]
            # checks if potential enemy has legal moves with kings position
            if self.board[row][col]:
                for pos in self.board[row][col].get_legal_moves(self.board, (row, col)):
                    if self.board[pos[0]][pos[1]]:
                        if self.board[pos[0]][pos[1]].rank == Rank.KING:
                            # in check
                            return True
        return False

    def move(self, current_pos, new_pos):
        piece = self.get_piece(current_pos)
        if piece:
            """
            TODO: (for me) change how we get a reference to board inside of each piece instance. It will be better (and cleaner)
            to have a reference to the board object instead of the board array in each piece. This will be a big re-factor, so I'm
            holding off on it for now
            """
            # Am I(piece) in check?
            if self.in_check(piece.team):
                # try a move to get out and see if piece's move is legal
                if piece.move(self.board, current_pos, new_pos):
                    # try to move it and see if my king is in check afterwards
                    self.board[current_pos[0]][current_pos[1]] = None
                    self.board[new_pos[0]][new_pos[1]] = piece
                    if self.in_check(piece.team):
                        # if I'm still in check after the switch, undo it return False
                        self.board[current_pos[0]][current_pos[1]] = piece
                        self.board[new_pos[0]][new_pos[1]] = None
                        print("Still in check")
                        self.display()
                        return False
            else:
                print("Looks good! Not in check")
                if piece.move(self.board, current_pos, new_pos):
                    self.board[current_pos[0]][current_pos[1]] = None
                    self.board[new_pos[0]][new_pos[1]] = piece
                    if self.in_check(piece.team):
                        self.board[current_pos[0]][current_pos[1]] = piece
                        self.board[new_pos[0]][new_pos[1]] = None
                        print("Can't move into check!")
                        self.display()
                        return False
                    else:
                        self.display()
                        return True
            self.display()
            return False

    # TODO: return team of winner, or None if the game needs to continue
    def is_game_over(self):
        if self.in_check(Team.WHITE):
            if self.try_all_legal_moves(Team.WHITE):
                return None
            else:
                return Team.BLACK
        elif self.in_check(Team.BLACK):
            if self.try_all_legal_moves(Team.BLACK):
                return None
            else:
                return Team.WHITE
        else:
            return None


board = Board()
board.move((1, 4), (3, 4))
board.move((6, 0), (4, 0))
board.move((7, 0), (5, 0))
board.move((5, 0), (5, 3))
board.move((5, 3), (2, 3))
board.move((2, 3), (2, 4))
board.move((0, 3), (1, 4))
board.move((1, 1), (2, 1))
board.move((1, 3), (2, 3))
bishop = board.board[0][2]
print(bishop.get_legal_moves(board.board, (0, 2)))
"""
rook = board.board[2][1]
print(rook)
rook.get_legal_moves(board.board, (2, 1))
"""
