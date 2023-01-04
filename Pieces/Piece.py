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
        # note: self.rank is assigned uniquely by each child class

    # note: good practice to keep the data members of a class hidden and only read/write to them via methods (i.e. getters/setters)
    def get_team(self):
        return self.team

    def is_white_team(self):
        return self.team == Team.WHITE

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
        # note: I like the format: Rook (W). What do you think? I like it and I made the pieces light blue to be easier to look at
        return "\033[1;36;40m{} ({})\033[0m".format(self.rank.name, self.team.name[0])
