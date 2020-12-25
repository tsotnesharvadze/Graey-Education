from enum import Enum
from abc import abstractmethod, ABCMeta
from typing import Tuple

import game


class Color(Enum):
    WHITE = 'WHITE'
    BLACK = 'BLACK'


class Piece(metaclass=ABCMeta):

    @property
    @abstractmethod
    def display(self):
        pass

    def __init__(self, color: Color):
        self.color = color

    @staticmethod
    def get_distance(start: 'game.Spot', end: 'game.Spot') -> Tuple[int, int]:
        return abs(start.y - end.y), abs(start.x - end.x)

    @abstractmethod
    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        # without distance method
        dy, dx = self.get_distance(start, end)
        if dy == dx == 0:
            return False

        if end and end.piece.color == self.color:
            return False

    def __str__(self):
        return self.display[self.color]


class Rook(Piece):
    # ეტლი
    display = {
        Color.WHITE: '♜',
        Color.BLACK: '♖',
    }

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        # @TODO: როცა ეღობება ფიგურა
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)
        return dy * dx == 0


class Pawn(Piece):
    # პაიკი
    pass


class Knight(Piece):
    # მხედარი

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)

        return dy * dx == 2


class Bishop(Piece):
    # კუ

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)
        return dy == dx


class King(Piece):
    # მეფე
    castled = False
    can_castle = True

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)

        return (dy + dx == 1) or (dx == 1 and dy == 1)


class Queen(Piece):

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, game)
        dy, dx = self.get_distance(start, end)
        return dy * dx == 0 or dy == dx
