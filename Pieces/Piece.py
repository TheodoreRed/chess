from enum import Enum


class Team(Enum):
    WHITE = 1
    BLACK = 2


class Piece:
    def __init__(self, team):
        self.team = team

    def __repr__(self):
        return "Piece"
