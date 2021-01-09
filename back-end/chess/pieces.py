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
        super().can_move(start, end, board)
        dy, dx = self.get_distance(start, end)

        if dy * dx != 0:
            return False
        elif dx != 0:
            start_x, end_x = sorted([start.x, end.x])
            return not any(board.board[start.y][start_x + 1:end_x])
        else:
            start_y, end_y = sorted([start.y, end.y])
            for y in range(start_y + 1, end_y):
                if board.get_spot(start.x, y):
                    return False

        return True


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

        elif dx > 0:
            return False

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
        dy, dx = end.y - start.y, end.x - start.x

        if abs(dx) != abs(dy):
            return False

        # Normalizing dx, dy to get directions
        # ნორმალიზება dx, dy ცვლადების რათა ფიგურის მოძრაობის მიმართულება გავიგოთ
        x_inc = dx // abs(dx)
        y_inc = dy // abs(dy)

        x, y = start.x, start.y
        for _ in range(abs(dx)):
            x += x_inc
            y += y_inc
            if board.get_spot(x, y):
                return False

        return True


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
        dy, dx = end.y - start.y, end.x - start.x,

        if dx * dy == 0:
            # behaves like Rook
            if dx != 0:
                start_x, end_x = sorted([start.x, end.x])
                return not any(board.board[start.y][start_x + 1:end_x])
            else:
                start_y, end_y = sorted([start.y, end.y])
                for y in range(start_y + 1, end_y):
                    if board.get_spot(start.x, y):
                        return False

        else:
            # behaves like bishop
            if abs(dx) != abs(dy):
                return False

            # Normalizing dx, dy to get directions
            # ნორმალიზება dx, dy ცვლადების რათა ფიგურის მოძრაობის მიმართულება გავიგოთ
            x_inc = dx // abs(dx)
            y_inc = dy // abs(dy)

            x, y = start.x, start.y
            for _ in range(abs(dx)):
                x += x_inc
                y += y_inc
                if board.get_spot(x, y):
                    return False

        return True
