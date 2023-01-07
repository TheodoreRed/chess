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

    """
    TODO: We shouldn't actually move any pieces as the result of this function. We only want to evaluate if the game is over or not.
    
    So, I propose changing this method's name to is_checkmate where it returns True at the bottom of the method if all of the potential moves fail
    to get your team out of check and it breaks early by returning False if any moves do get you out of check

    If the game continues, then the player in check knows for sure they have a way to save themselves and if the game ends... GG!
    """
    # trys all the legal moves on a team. if it finds one that stops check returns true
    def try_all_legal_moves(self, team):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] != None:
                    piece = self.board[row][col]
                    if piece.team == team:
                        piece_moves = piece.get_legal_moves(self.board, (row, col))
                        for move in piece_moves:
                            # TODO: the variable move is already a tuple. no need to split it up, just pass it directly!
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

    # TODO: generalize this to get any particular piece i.e. (get_position(self, team, rank)). might come in handy later and the code is already here
    def get_kings_position(self, team):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] != None:
                    piece = self.board[row][col]
                    if piece.rank == Rank.KING and piece.team == team:
                        return (row, col)

    # check if a team is in check
    def in_check(self, team):
        '''
        TODO: don't forget to use tuple notation. THIS CAN BE CHANGED BASICALLY EVERYWHERE AND I SUGGEST YOU DO FOR CLEANLINESS

        x, y = get_my_tuple() automatically splits the tuple apart into x and y
        instead of x, y = my_tuple[0], my_tuple[1]

        so in this case: "king_row, king_pos = self.get_kings_position(team)"
        '''
        king_pos = self.get_kings_position(team)
        king_row = king_pos[0]
        king_col = king_pos[1]

        test_queen = Queen(team)
        test_knight = Knight(team)

        '''
        note: this took me a while to figure out, probably worth commenting. I see now that: all of the potential movements of a queen/knight from the king's position would
        include all of the enemy positions on the board that could threaten the king... a bit confusing but very clever and efficient!
        '''
        potential_enemies = test_queen.get_legal_moves(self.board, (king_row, king_col))
        potential_enemies.extend(test_knight.get_legal_moves(self.board, (king_row, king_col)))

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

            # note: would it be more accurate to ask: is my team in check? (splitting hairs)
            # Am I (piece) in check?
            if self.in_check(piece.team):
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
                    if self.in_check(piece.team):
                        self.board[current_pos[0]][current_pos[1]] = piece
                        self.board[new_pos[0]][new_pos[1]] = None
                        print("Can't move into check!")
                        return False
                    else:
                        self.display()
                        piece.first_move = False
                        return True
            return False

    # TODO: return team of winner, or None if the game needs to continue
    def is_game_over(self):
        # TODO: DRY this shit out ;) the if and elif branches here are identical. You just need to establish team and enemy_team variables. Easy enough w/ ternary operators
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
            # TODO: Get rid of this else branch. A function always returns None by default
            return None


"""
board = Board()
board.move((1, 4), (3, 4))
board.move((0, 5), (3, 2))
board.move((0, 3), (4, 7))
board.move((3, 2), (6, 5))
piece = board.board[3][4]
print(piece.get_legal_moves(board.board, (3, 4)))
print()
print(board.is_game_over())
"""
