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
        if (start is end) or (end and end.piece.color == self.color):
            return False

    def moved(self, ):
        pass

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
    display = {
        Color.BLACK: '♙',
        Color.WHITE: '♟'
    }

    direction = {
        Color.WHITE: -1,
        Color.BLACK: 1
    }

    initial = True

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy = self.direction[self.color] * (start.y - end.y)
        dx = abs(start.x - end.x)

        if dy <= 0:
            return False

        elif end and end.piece.color != self.color:
            return abs(dx) == dy == 1

        elif self.initial:
            return 0 < dy <= 2

        return 0 < dy <= 1

    def moved(self, ):
        self.initial = False


class Knight(Piece):
    display = {
        Color.WHITE: '♞',
        Color.BLACK: '♘',
    }

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)

        return dy * dx == 2


class Bishop(Piece):
    display = {
        Color.WHITE: '♝',
        Color.BLACK: '♗',
    }

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)
        return dy == dx


class King(Piece):
    display = {
        Color.WHITE: '♚',
        Color.BLACK: '♔',
    }
    # მეფე
    castled = False
    can_castle = True

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)

        return (dy + dx == 1) or (dx == 1 and dy == 1)

    def moved(self, ):
        self.can_castle = False


class Queen(Piece):
    display = {
        Color.WHITE: '♕',
        Color.BLACK: '♛',
    }

    def can_move(self, start: 'game.Spot', end: 'game.Spot', board: 'game.Board'):
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)
        return dy * dx == 0 or dy == dx
