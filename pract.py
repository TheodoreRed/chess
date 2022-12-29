import os

os.system("cls")
BOARD_SIZE = 8
"""
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7, 7, 7, 7],
]"""
board = {"a": {}, "b": {}, "c": {}, "d": {}, "e": {}, "f": {}, "g": {}}
for row in board:
    row = {"1": None, "2": None}


def display(board):
    for row in board:
        for col in row:
            print(board[row][col])


display(board)
