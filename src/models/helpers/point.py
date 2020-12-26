from constants import BOARD_HEIGHT, BOARD_WIDTH


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_equal(self, other):
        return self.x == other.x and self.y == other.y

    def is_valid(self):
        """Determine if this point is within the bounds of the board."""
        return (
            0 <= self.x
            and self.x < BOARD_WIDTH
            and 0 <= self.y
            and self.y < BOARD_HEIGHT
        )
