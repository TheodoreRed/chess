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
    [Rook(Team.WHITE), Knight(Team.WHITE), Bishop(Team.WHITE), Queen(Team.WHITE), King(Team.WHITE), Bishop(Team.WHITE), Knight(Team.WHITE), Rook(Team.WHITE)],
    [Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE), Pawn(Team.WHITE)],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK), Pawn(Team.BLACK)],
    [Rook(Team.BLACK), Knight(Team.BLACK), Bishop(Team.BLACK), Queen(Team.BLACK), King(Team.BLACK), Bishop(Team.BLACK), Knight(Team.BLACK), Rook(Team.BLACK)],
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

    # trys all the legal moves on a team. if it finds one that stops check returns False
    def is_checkmate(self, team):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col]:
                    piece = self.board[row][col]
                    if piece.team == team:
                        piece_moves = piece.get_legal_moves(self.board, (row, col))
                        for move in piece_moves:
                            if piece.move(self.board, (row, col), move):
                                self.board[row][col] = None
                                self.board[move[0]][move[1]] = piece
                                if not self.in_check(piece.team):
                                    self.board[row][col] = piece
                                    self.board[move[0]][move[1]] = None
                                    # found a spot that would get out of check
                                    return False
                                else:
                                    self.board[row][col] = piece
                                    self.board[move[0]][move[1]] = None
        return True

    def get_ranks_position(self, team, rank):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col]:
                    piece = board.get_piece((row, col))
                    if piece:
                        if piece.rank == rank and piece.team == team:
                            return (row, col)

    # check if a team is in check
    def in_check(self, team):
        king_row, king_col = self.get_ranks_position(team, Rank.KING)

        test_queen = Queen(team)
        test_knight = Knight(team)

        # get all legal moves for queen and knight from king's position  
        # these positions represent potential enemy positions
        potential_enemies = test_queen.get_legal_moves(self.board, (king_row, king_col))
        potential_enemies.extend(test_knight.get_legal_moves(self.board, (king_row, king_col)))
        print(potential_enemies)
        # iterate over potential enemy positions
        for position in potential_enemies:
            row, col = position
            # if there is a piece at potential enemy position
            if self.board[row][col]:
                # get legal moves for that piece
                for pos in self.board[row][col].get_legal_moves(self.board, (row, col)):
                    print(pos)
                    # check if any legal moves are the position of the king
                    if self.board[pos[0]][pos[1]]:
                        if board.get_piece(pos).rank == Rank.KING:
                            # in check
                            return True
        # if loop completes and no legal moves of potential enemies threaten king, team is not in check
        return False

    def move(self, current_pos, new_pos):
        piece = self.get_piece(current_pos)
        if piece:
            """
            TODO: (for me) change how we get a reference to board inside of each piece instance. It will be better (and cleaner)
            to have a reference to the board object instead of the board array in each piece. This will be a big re-factor, so I'm
            holding off on it for now
            """

            # Is my team in check?
            if self.in_check(piece.get_team()):
                # try a move to get out and see if piece's move is legal
                if piece.move(self.board, current_pos, new_pos):
                    # try to move it and see if my king is in check afterwards
                    '''
                    TODO: This logic about: am i in check -> try to move out -> still in check: is all sound and well written. Only problem is that it isn't very DRY.
                    I think a good re-factor would be a method like: Board::take_piece(current_pos, new_pos) that does this piece of 2-line logic

                    And later when you undo the switch because they're still in check, just use the same method with reversed parameters

                    If it seems like overkill, just think about how literal this function would become to read:
                        if in_check:
                            try_to_move():
                                take_piece()
                                if in_check:
                                    take_piece()
                                    return
                    
                    Python really is the GOAT of readability (if you move all of your logic out into indivdual methods)
                    '''
                    self.board[current_pos[0]][current_pos[1]] = None
                    self.board[new_pos[0]][new_pos[1]] = piece
                    if self.in_check(piece.team):
                        # if I'm still in check after the switch, undo it return False
                        self.board[current_pos[0]][current_pos[1]] = piece
                        self.board[new_pos[0]][new_pos[1]] = None
                        print("Still in check")
                        return False
            else:
                if piece.move(self.board, current_pos, new_pos):
                    self.board[current_pos[0]][current_pos[1]] = None
                    self.board[new_pos[0]][new_pos[1]] = piece
                    if self.in_check(piece.get_team()):
                        self.board[current_pos[0]][current_pos[1]] = piece
                        self.board[new_pos[0]][new_pos[1]] = None
                        print("Can't move into check!")
                        return False
                    else:
                        self.display()
                        piece.first_move = False
                        return True
            return False

    def is_game_over(self, team):
        if self.in_check(team):
            if self.is_checkmate(team):
                winner = Team.BLACK if team == Team.WHITE else Team.WHITE
                return winner



board = Board()
board.move((1, 4), (3, 4))
board.move((0, 5), (3, 2))
board.move((0, 3), (4, 7))
board.move((3, 2), (6, 5))
print(board.in_check(Team.BLACK))