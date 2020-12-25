import enum


class Color(enum):
    WHITE = 'WHITE'
    BLACK = 'BLACK'


class Piece:
    def __init__(self, color: Color):
        self.color = color

    def __str__(self):
        pass


class Rook(Piece):
    display = {
        Color.WHITE: '♜',
        Color.BLACK: '♖',
    }
    pass


class King(Piece):
    pass
