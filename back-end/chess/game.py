from typing import List

from pieces import *


class Spot:
    def __init__(self, x: int, y: int, piece: 'Piece' = None):
        self.x = x
        self.y = y
        self.piece = piece

    def __bool__(self):
        return self.piece is not None


class Board:
    def __init__(self):
        self.board: 'List[List[Spot]]' = []

        self.board.append([
            Spot(0, 0, Rook(Color.WHITE)),
            Spot(0, 1, Knight(Color.WHITE)),
            Spot(0, 2, Bishop(Color.WHITE)),
            Spot(0, 3, Queen(Color.WHITE)),
            Spot(0, 4, King(Color.WHITE)),
            Spot(0, 5, Bishop(Color.WHITE)),
            Spot(0, 6, Knight(Color.WHITE)),
            Spot(0, 7, Rook(Color.WHITE))
        ])
        self.board.append([
            Spot(1, 0, Pawn(Color.WHITE)),
            Spot(1, 0, Pawn(Color.WHITE)),
            Spot(1, 2, Pawn(Color.WHITE)),
            Spot(1, 3, Pawn(Color.WHITE)),
            Spot(1, 4, Pawn(Color.WHITE)),
            Spot(1, 5, Pawn(Color.WHITE)),
            Spot(1, 6, Pawn(Color.WHITE)),
            Spot(1, 7, Pawn(Color.WHITE)),
        ])

        for i in range(2, 6):
            self.board.append([
                Spot(i, j) for j in range(0, 8)
            ])

        self.board.append([
            Spot(6, 0, Pawn(Color.BLACK)),
            Spot(6, 0, Pawn(Color.BLACK)),
            Spot(6, 2, Pawn(Color.BLACK)),
            Spot(6, 3, Pawn(Color.BLACK)),
            Spot(6, 4, Pawn(Color.BLACK)),
            Spot(6, 5, Pawn(Color.BLACK)),
            Spot(6, 6, Pawn(Color.BLACK)),
            Spot(6, 7, Pawn(Color.BLACK)),
        ])

        self.board.append([
            Spot(7, 0, Rook(Color.BLACK)),
            Spot(7, 1, Knight(Color.BLACK)),
            Spot(7, 2, Bishop(Color.BLACK)),
            Spot(7, 3, Queen(Color.BLACK)),
            Spot(7, 4, King(Color.BLACK)),
            Spot(7, 5, Bishop(Color.BLACK)),
            Spot(7, 6, Knight(Color.BLACK)),
            Spot(7, 7, Rook(Color.BLACK))
        ])

    def __str__(self):
        board = "   ---------------------------------------"
        for y in range(7, -1, -1):
            board += f'\n {y + 1}|'
            for x in range(0, 8):
                board += f' [{self.board[y][x]}] '
        board += "\n   ---------------------------------------\n"
        board += '     A    B    C    D    E    F    G    H'
        return board

    def get_spot(self, x, y):
        # @TODO: return if possible
        return self.board[y][x]
