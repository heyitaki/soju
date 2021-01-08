from __future__ import annotations

from typing import Final

import src.models.points.offset_point


class CubePoint:
    x: Final[int]
    y: Final[int]
    z: Final[int]

    def __init__(self, x: int, y: int, z: int = None):
        self.x = x
        self.y = y
        self.z = -x - y if z is None else z

        if z is not None and not (x + y + z == 0):
            raise Exception("Tried to init CubePoint with invalid coordinates")

    def __add__(self, other) -> CubePoint:
        if isinstance(other, CubePoint):
            return CubePoint(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, src.models.points.offset_point.OffsetPoint):
            return self + other.to_cube()
        else:
            raise ValueError

    def __eq__(self, other):
        if isinstance(other, CubePoint):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif isinstance(other, src.models.points.offset_point.OffsetPoint):
            return self == other.to_cube()
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __mul__(self, other):
        if isinstance(other, int):
            return CubePoint(self.x * other, self.y * other)
        else:
            raise ValueError

    def __repr__(self):
        if False:
            return str(self.to_offset())
        return f"CubePoint(x={self.x}, y={self.y}, z={self.z})"

    def to_offset(self) -> src.models.points.offset_point.OffsetPoint:
        x = self.x + (self.y + self.y % 2) // 2
        y = self.y
        return src.models.points.offset_point.OffsetPoint(x, y)
