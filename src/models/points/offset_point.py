from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.points.cube_point import CubePoint


class OffsetPoint:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def from_cube(cls, cp: CubePoint):
        x = round(cp.x + (cp.z + cp.z % 2) / 2)
        y = round(cp.z)
        return cls(x, y)
