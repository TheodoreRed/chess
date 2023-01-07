try:
    from Pieces.Piece import *
    from Pieces.Bishop import *
    from Pieces.Rook import *
except:
    from Piece import *


class Queen(Piece):
    def __init__(self, team):
        Piece.__init__(self, team)
        self.rank = Rank.QUEEN

    """
    def get_legal_moves(self, board, position):
        legal_moves = []
        bishop = Bishop(self.team)
        for move in bishop.get_legal_moves(board, (position[0], position[1])):
            legal_moves.append(move)
        rook = Rook(self.team)
        for move in rook.get_legal_moves(board, (position[0], position[1])):
            legal_moves.append(move)
        return legal_moves
    """

    def move(self, board, current_pos, new_pos):
        bishop = Bishop(self.team)
        rook = Rook(self.team)

        # note: so goddamn clean... just look at this. wow...
        if bishop.move(board, current_pos, new_pos) or rook.move(board, current_pos, new_pos):
            return True
        else:
            """
            TODO: There's a problem with error messaging here! I know that probably nobody but us will play this game but still... it's such an important skill!
            And it's one I will harp on as we collaborate because you only learn about error messaging by working with others. You always know how to work with your code correctly
            but it's easier for a third party (like myself) to identify potential breaking points. I'm treating this meaningless task as a learning exercise

            Anyways: the problem is that bishop::move and rook::move will print out their own messages, even if they return false. Which causes 2 subproblems:
            
            Problem a) bishop/rook printed out a useful error message like 'your own piece is blocking the path' then we negate it below by saying 'Queens can only move...'
            but what if they already tried to move diagonally? they understands how queens move, there's just a piece in the way!

            Problem b) we're trying to move the queen like a bishop and the rook says 'rooks can only move in a straight line'... huh?? I'm not moving a rook!? This is a queen
            and I'm moving it diagonally!

            Solution: it's a design choice. What do you think? We should discuss it on Discord
            """
            print("Try again: Queens can only move along straight lines and diagonals.")
            return False
