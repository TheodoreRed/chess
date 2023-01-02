"""
note: this is fine to leave in for now. When you're running Board.py you're in the top level directory so you need to go through
the sub-folder (Pieces.Piece) but when you're running Rook.py directly you're already in the Pieces folder

in other words: you only need this because you run code from Rook.py directly. You're only doing that to debug, which is fine. 
But in the 'production' version of this game, you'll only ever call this code from Board.py and you won't need the bottom case
"""
try:
    from Pieces.Piece import *
except:
    from Piece import *


class Rook(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.ROOK

        # TODO: multiple pieces use first_move and it'll start as True no matter what. Move it to the parent class
        self.first_move = True

    def move(self, board, current_pos, new_pos):
        # TODO: update these to use streamlined declaration i.e. new_row, new_col = new_pos
        new_row = new_pos[0]
        new_col = new_pos[1]
        current_row = current_pos[0]
        current_col = current_pos[1]

        # Vertical Change
        if new_col == current_col:
            # Up or Down
            route = 1 if new_row > current_row else -1
            for i in range(current_row + route, new_row + route, route):
                if board[i][new_col] != None:
                    """
                    note: the keyword 'is' checks if two variables refer to the *exact* same object. '==' just checks if they're equivalent.
                    it's good to use this here because Team.WHITE and Team.WHITE are the exact same object, but just make sure
                    you acknowledge the difference between 'is' and '=='

                    i.e.
                    0 is not False
                    0 == False

                    Team.WHITE is Team.WHITE
                    Team.WHITE == Team.WHITE
                    """
                    if board[i][new_col].team is self.team:
                        # TODO: Mirror my error messaging in Game.py i.e. "Try again: one of your pieces is in the way" (or something like that)
                        print("Same team!")
                        return False
                    elif i != new_row:
                        # TODO: Update the error messaging like above, and make sure to include that it's an *enemy* piece in our way
                        print("Piece in the way")
                        return False
                    
                    """
                    TODO: Remove this 'return True'. It's redundant. This will only run if there's an enemy piece on the last iteration of the loop.
                    In other words, if our new_pos has an enemy on it and we can move there. In that case, the loop will end and we'll just
                    return True anyway
                    """
                    return True
            return True

        # Horizontal Change
        if new_row == current_row:
            # Left or Right
            route = 1 if new_col > current_col else -1
            for i in range(current_col + route, new_col + route, route):
                if board[new_row][i] != None:
                    if board[new_row][i].team is self.team:
                        print("Same Team!")
                        return False
                    else:
                        if i != new_col:
                            print("Piece in the way")
                            return False
                    return True
            return True

        # TODO: Beef up error messaging, I won't comment on every error message in the whole game but I think you see what I mean
        print("Not same row or column")
        return False
