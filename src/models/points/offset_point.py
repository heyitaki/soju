from __future__ import annotations

from typing import Final

# Get rid of circular import
import src.models.points.cube_point


class OffsetPoint:
    x: Final[float]
    y: Final[float]

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

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

    def to_cube(self) -> src.models.points.cube_point.CubePoint:
        x = self.x - (self.y + self.y % 2) / 2
        z = self.y
        y = -x - z
        return src.models.points.cube_point.CubePoint(x, y, z)
