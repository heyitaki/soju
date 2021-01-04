from typing import Final
from __future__ import annotations
from src.models.points.offset_point import OffsetPoint


class CubePoint:
    x: Final[float]
    y: Final[float]
    z: Final[float]

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def to_offset(self) -> OffsetPoint:
        x = self.x + (self.z + self.z % 2) / 2
        y = self.z
        return OffsetPoint(x, y)
