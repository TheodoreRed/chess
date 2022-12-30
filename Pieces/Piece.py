from enum import Enum


class Team(Enum):
    WHITE = 1
    BLACK = 2


class Piece:
    def __init__(self, team, position):
        self.team = team
        self.position = position

    def __repr__(self):
        return "Piece"
