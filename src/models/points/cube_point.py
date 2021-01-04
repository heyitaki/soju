from __future__ import annotations

from typing import Final

import src.models.points.offset_point


class CubePoint:
    x: Final[float]
    y: Final[float]
    z: Final[float]

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if isinstance(other, CubePoint):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, src.models.points.offset_point.OffsetPoint):
            return self == other.to_cube()
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"CubePoint(x={self.x}, y={self.y}, z={self.z})"

    def to_offset(self) -> src.models.points.offset_point.OffsetPoint:
        x = self.x + (self.z + self.z % 2) / 2
        y = self.z
        return src.models.points.offset_point.OffsetPoint(x, y)
