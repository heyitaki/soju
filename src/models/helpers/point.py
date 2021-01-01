from src.constants import BOARD_HEIGHT, BOARD_WIDTH


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_equal(self, other):
        return self.x == other.x and self.y == other.y
