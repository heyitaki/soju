from __future__ import annotations

from math import sqrt
from typing import Final

# Get rid of circular import
import src.models.points.cube_point


class OffsetPoint:
    x: Final[int]
    y: Final[int]

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other) -> src.models.points.cube_point.CubePoint:
        if isinstance(other, OffsetPoint):
            return self.to_cube() + other.to_cube()
        elif isinstance(other, src.models.points.cube_point.CubePoint):
            return self.to_cube() + other
        else:
            raise ValueError

    def __eq__(self, other):
        if isinstance(other, OffsetPoint):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, src.models.points.cube_point.CubePoint):
            return self == other.to_offset()
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"OffsetPoint(x={self.x}, y={self.y})"

    def to_cartesian(self):
        """
        Convert this point to a cartesian coordinate.

        The width of a hexagon (pointy top) with side length 1 is sqrt(3) while the height is 2. We
        can get cartesian coordinates with the following formulas:

            dx = .5w if y % 2 == 1 else 0,
            newX = .5w + xw + dx,
            newY = .5h + .75yh,

        where (newX, newY) is our cartesian coordinate, (x, y) is the offset coordinate, dx is the
        shift in indented rows and w and h are the width and height of the hexagon respectively.
        """
        w = 1.73205  # sqrt(3)
        h = 2
        dx = 0.5 * w if self.y % 2 == 1 else 0
        x = 0.5 * w + self.x * w + dx
        y = 0.5 * h + 0.75 * self.y * h
        return (x, y)

    def to_cube(self) -> src.models.points.cube_point.CubePoint:
        x = self.x - (self.y + self.y % 2) // 2
        y = self.y
        return src.models.points.cube_point.CubePoint(x, y)
