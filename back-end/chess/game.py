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
    def __int__(self):
        self.board: 'List[List[Spot]]' = []

    def get_spot(self, x, y):
        # @TODO: return if possible
        return self.board[y][x]
