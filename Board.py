from copy import deepcopy

from GUI import GUI
from Pieces.Piece import Team, Rank
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Knight import Knight

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
        self.gui = GUI()

    def populate_board(self, starting_board):
        self.board = deepcopy(starting_board)

    def display(self):
        """
        print("---------------------------")
        for row in reversed(range(len(self.board))):
            print(self.board[row])

        print("---------------------------")   
        """
        self.gui.draw_board(self.board)

    def get_board(self):
        return self.board

    def get_piece(self, pos):
        return self.board[pos[0]][pos[1]]
    
    # note: just adding this method for readability
    def attack_position(self, current_pos, new_pos, attacking_piece):
        current_row, current_col = current_pos
        new_row, new_col = new_pos

        self.board[current_row][current_col] = None
        self.board[new_row][new_col] = attacking_piece

    # tries all the legal moves on a team. if it finds one that stops check returns False
    def is_checkmate(self, team):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.board[row][col]
                piece_pos = (row, col)

                if piece and piece.team == team:
                    piece_moves = piece.get_legal_moves(self.board, piece_pos)
                    # note: no need to check piece.move() because we already know this move is legal
                    for move in piece_moves:
                        # only changing board state to re-evaluate check. always revert board state below
                        self.attack_position(piece_pos, move, piece)

                        if not self.in_check(piece.team):
                            # found a spot that would get out of check
                            self.attack_position(move, piece_pos, piece)
                            return False
                        else:
                            self.attack_position(move, piece_pos, piece)

        return True

    def get_ranks_position(self, team, rank):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.get_piece((row, col))
                if piece and piece.rank == rank and piece.team == team:
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

        # print(potential_enemies)

        # iterate over potential enemy positions
        for position in potential_enemies:
            row, col = position
            # if there is a piece at potential enemy position
            if self.board[row][col]:
                # get legal moves for that piece
                for pos in self.board[row][col].get_legal_moves(self.board, (row, col)):
                    # check if any legal moves are the position of the king
                    if self.board[pos[0]][pos[1]]:
                        if self.get_piece(pos).rank == Rank.KING:
                            # in check
                            return True
        # if loop completes and no legal moves of potential enemies threaten king, team is not in check
        return False

    def move(self, current_pos, new_pos):
        piece = self.get_piece(current_pos)

        if not piece:
            return False
        
        team_in_check = self.in_check(piece.get_team())
        if team_in_check:
            print("You're in check!")

        if piece.move(self.board, current_pos, new_pos):
            self.attack_position(current_pos, new_pos, piece)

            if self.in_check(piece.get_team()):
                self.attack_position(new_pos, current_pos, piece)
                print("Try again: you can't move into check!" if not team_in_check else "Try again: you're still in check!")
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
print(board.is_game_over(Team.BLACK))
