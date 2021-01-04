from __future__ import annotations

from typing import Final

from src.models.points.cube_point import CubePoint


class OffsetPoint:
    x: Final[float]
    y: Final[float]

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_cube(self) -> CubePoint:
        x = self.x - (self.y + self.y % 2) / 2
        z = self.y
        y = -x - z
        return CubePoint(x, y, z)
