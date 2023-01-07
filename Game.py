from Board import Board
from Pieces.Piece import Team


LETTER_TO_COL = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


class Game:
    def __init__(self):
        self.board = Board()
        self.current_team = Team.WHITE
        self.game_over = False

    def start_game(self):
        while not self.game_over:
            self.handle_input()

    def handle_input(self):
        self.board.display()
        print("{}'S TURN".format(self.current_team.name))
        print()

        current_pos_input, current_pos = None, None
        while not current_pos:
            current_pos_input = input("What piece do you want to move? (format: a1) ").lower()
            current_pos = self.convert_input_to_coordinates(current_pos_input)

            piece = self.board.get_piece(current_pos)

            if not piece:
                print("Try again: there is no piece at {}".format(current_pos_input))
                current_pos = None
            elif piece.get_team() != self.current_team:
                print("Try again: wrong team. You do not control the piece at {}".format(current_pos_input))
                current_pos = None

        new_pos_input, new_pos = None, None
        while not new_pos:
            new_pos_input = input("Where do you want to move this piece? (format: a1) ").lower()
            new_pos = self.convert_input_to_coordinates(new_pos_input)

        if self.board.move(current_pos, new_pos):
            print()
            print("Moved {} from {} to {}".format(self.board.get_piece(new_pos), current_pos_input, new_pos_input))

            self.finish_turn()

    """
    note: this method doesn't need a reference to 'self' BUT it is used by this class. In that way, this method isn't associated
    with each *instance* of the class but only with the class itself. This type of method is called static. Look up 'static methods'
    to learn more about them in general (important concept in any OOP langauge)
    """
    @staticmethod
    def convert_input_to_coordinates(input):
        if len(input) != 2:
            print("Try again: input needs to be exactly 2 characters")
            return None

        col_letter, row_number = input[0], input[1]

        if not col_letter.isalpha():
            print("Try again: column needs to be a letter. Got {} instead".format(col_letter))
            return None

        if col_letter not in LETTER_TO_COL.keys():
            print("Try again: column letter needs to be between a-h. Got {} instead".format(col_letter))
            return None

        if not row_number.isnumeric():
            print("Try again: row needs to be a number. Got {} instead".format(row_number))
            return None

        row_number = int(row_number)

        if row_number < 1 or row_number > 8:
            print("Try again: row needs to be between 1-8. Got {} instead".format(row_number))
            return None

        coordinates = (row_number - 1, LETTER_TO_COL[col_letter])

        return coordinates

    def finish_turn(self):
        check_team = self.current_team
        self.current_team = (Team.WHITE if self.current_team == Team.BLACK else Team.BLACK)
        print("--------")

        self.check_game_over(check_team)

    def check_game_over(self, team):
        winner = self.board.is_game_over(team)

        if winner:
            self.game_over = True

            print("GAME OVER: {} WINS".format(winner.name))
            print()


game = Game()
game.start_game()
