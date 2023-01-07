from enum import Enum


class Team(Enum):
    WHITE = 1
    BLACK = 2
    STALEMATE = 3


class Rank(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


class Piece:
    def __init__(self, team):
        self.team = team
        self.first_move = True

    # note: good practice to keep the data members of a class hidden and only read/write to them via methods (i.e. getters/setters)
    def get_team(self):
        return self.team

    def is_white_team(self):
        return self.team == Team.WHITE

    """
    note: I regret to inform you: this is probably the cleanest way to write this function. Sorry you wrote a specific implementation for each piece.
    This is probably a bit less efficient but I feel confident that the move() method of each piece fails quickly if the move is impossible
    (like if a rook move isn't straight, or a bishop move isn't diagonal, etc)
    """
    def get_legal_moves(self, board, current_pos):
        empty_positions = []

        for row in range(len(board)):
            for col in range(len(board)):
                if not board[row][col]:
                    empty_positions.append((row, col))
        
        legal_moves = []
        for empty_pos in empty_positions:
            if self.move(board, current_pos, empty_pos):
                legal_moves.append(empty_pos)
        return legal_moves

    """
    note: we talked about this but as a refresher:

    by default, if you run '==' between two objects it just checks if it's the *exact* same object.
    In that case, if we made two brand new white rooks, they wouldn't be equal... cause they're different objects.

    If we change this __eq__ dunder method to have a different definition of equality then we can say this instead:
    if two pieces have the same team and rank then they are equivalent
    """
    def __eq__(self, other):
        return other and self.team == other.team and self.rank == other.rank

    def __repr__(self):
        return "\033[1;36;40m{} ({})\033[0m".format(self.rank.name, self.team.name[0])
