from typing import Final

from src.constants import BOARD_HEIGHT, BOARD_WIDTH


class Point:
    x: Final[int]
    y: Final[int]

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
