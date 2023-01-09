import tkinter as tk
from PIL import Image, ImageTk

from Pieces.Piece import Team, Rank

BOARD_SIZE = 8
BOARD_SQUARE_SIZE = 60
CANVAS_SIZE = BOARD_SQUARE_SIZE * BOARD_SIZE

SQUARE_COLOR = { Team.WHITE: 'white', Team.BLACK: 'gray' }


root = tk.Tk()
root.title("Redlon Chess")

canvas = tk.Canvas(root, height=CANVAS_SIZE, width=CANVAS_SIZE)
canvas.pack()


class GUI:

    def draw_board(self, board):
        color = SQUARE_COLOR[Team.BLACK]

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                square_point1_x = row * BOARD_SQUARE_SIZE
                square_point1_y = (CANVAS_SIZE - BOARD_SQUARE_SIZE) - (col * BOARD_SQUARE_SIZE)

                square_point2_x = square_point1_x + BOARD_SQUARE_SIZE
                square_point2_y = square_point1_y + BOARD_SQUARE_SIZE

                canvas.create_rectangle((square_point1_x, square_point1_y, square_point2_x, square_point2_y), fill=color)

                piece = board[col][row]
                if piece:
                    self.draw_piece_image(piece, (square_point1_x, square_point1_y), color)

                color = SQUARE_COLOR[Team.BLACK] if color == SQUARE_COLOR[Team.WHITE] else SQUARE_COLOR[Team.WHITE]

            color = SQUARE_COLOR[Team.BLACK] if color == SQUARE_COLOR[Team.WHITE] else SQUARE_COLOR[Team.WHITE]

        root.mainloop()
    
    def draw_piece_image(self, piece, loc, square_color):
        path = "./images/{}_{}.png".format(piece.team.name.lower(), piece.rank.name.lower())

        piece_image = Image.open(path)

        piece_photo_image = ImageTk.PhotoImage(piece_image)

        piece_label = tk.Label(image=piece_photo_image, bg=square_color, height=50, width=50)
        piece_label.image = piece_photo_image

        loc_x, loc_y = loc
        piece_label.place(x=loc_x + 5, y=loc_y + 5)