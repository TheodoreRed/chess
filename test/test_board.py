import sys
# import pytest

sys.path.append('./')

from Board import Board
from Pieces.Piece import Team
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Knight import Knight


PAWNLESS_BOARD = [
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
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
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


def test_move_rook_bad_input():
    # different column
    starting_board = PAWNLESS_BOARD
    result_board = PAWNLESS_BOARD

    board = Board(starting_board)
    print("---------Testing bad input---------")
    board.display()
    # board.move((0, 0), (3, 1))
    # board.display()
    assert board.get_board() == result_board


def test_move_rook_forwards():
    print("---------Forwards---------")

    print("---------Testing same team piece in the way---------")
    # same team piece in the way
    starting_board = PAWNLESS_BOARD
    result_board = [
        [
            None,
            Knight(Team.WHITE),
            Bishop(Team.WHITE),
            Queen(Team.WHITE),
            King(Team.WHITE),
            Bishop(Team.WHITE),
            Knight(Team.WHITE),
            Rook(Team.WHITE),
        ],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Rook(Team.WHITE), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
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
    board = Board(starting_board)
    board.move((0, 0), (3, 0))
    assert board.get_board() == result_board

    print("---------Testing enemy piece in the way---------")
    starting_board = PAWNLESS_BOARD
    result_board = [
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
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Rook(Team.WHITE), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
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

    board = Board(starting_board)
    board.board[4][0] = Rook(Team.WHITE)
    board.move((0, 0), (5, 0))
    assert board.get_board() == result_board

    print("---------Testing clear path---------")
    starting_board = PAWNLESS_BOARD
    result_board = [
        [
            None,
            Knight(Team.WHITE),
            Bishop(Team.WHITE),
            Queen(Team.WHITE),
            King(Team.WHITE),
            Bishop(Team.WHITE),
            Knight(Team.WHITE),
            Rook(Team.WHITE),
        ],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Rook(Team.WHITE), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
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

    board = Board(starting_board)
    board.move((0, 0), (3, 0))
    assert board.get_board() == result_board


def test_move_rook_backwards():
    print("---------Backwards---------")
    print("---------Testing same team in the way---------")
    # same team piece in the way
    start_board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, King(Team.BLACK), None, None, None, None],
    ]
    board = Board(start_board)
    board.board[7][7] = Rook(Team.BLACK)
    board.board[6][7] = Rook(Team.BLACK)
    #board.display()
    board.move((7, 7), (1, 7))

    result_board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(Team.BLACK)],
        [None, None, None, King(Team.BLACK), None, None, None, Rook(Team.BLACK)],
    ]
    assert board.get_board() == result_board
    print("---------Testing enemy piece in the way---------")
    # enemy team piece in the way
    board = Board(start_board)
    board.board[7][7] = Rook(Team.BLACK)
    board.board[6][7] = Rook(Team.WHITE)
    #board.display()
    board.move((7, 7), (1, 7))

    result_board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(Team.WHITE)],
        [None, None, None, King(Team.BLACK), None, None, None, Rook(Team.BLACK)],
    ]
    assert board.get_board() == result_board
    print("---------Testing clear path---------")
    # clear path
    board = Board(start_board)
    board.board[7][7] = Rook(Team.BLACK)
    board.move((7, 7), (5, 7))
    #board.display()

    result_board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(Team.BLACK)],
        [None, None, None, None, None, None, None, None],
        [None, None, None, King(Team.BLACK), None, None, None, None],
    ]
    assert board.get_board() == result_board
    pass


def test_move_rook_left():
    # same team piece in the way
    # enemy team piece in the way
    # clear path
    pass


def test_move_rook_right():
    # same team piece in the way
    # enemy team piece in the way
    # clear path
    pass


def test_rook():
    print("---------Testing Rook---------")
    test_move_rook_bad_input()
    # test_move_rook_forwards()
    # test_move_rook_backwards()
    # test_move_rook_left()
    # test_move_rook_right()


def test_checkmate():
    starting_board = [
        [None, None, None, King(Team.WHITE), None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, Rook(Team.WHITE), None, None],
        [Rook(Team.WHITE), None, None, None, None, None, None, King(Team.BLACK)],
    ]

    board = Board(starting_board)
    winner = board.is_game_over(Team.BLACK)
    assert winner == Team.WHITE

    starting_board = PAWNLESS_BOARD

    board = Board(starting_board)
    board.display()
    winner = board.is_game_over(Team.BLACK)
    assert winner == None


def test_board():
    test_rook()
    test_checkmate()
