from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Optional, Union

from src.models.points.cube_point import CubePoint as Cube
from src.models.points.offset_point import OffsetPoint as Offset
from src.models.points.offset_point import offset
from src.models.points.point import Point

if TYPE_CHECKING:
    from src.models.champion import Champion


class HexBoard:
    """"""

    height: int
    hexes: List[List[Optional[Champion]]]
    width: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.hexes = [[None for _ in range(width)] for _ in range(height)]

    def get(self, pos: Offset) -> Optional[Champion]:
        try:
            return self.hexes[pos.y][pos.x]
        except:
            return None

    def set(self, pos: Offset, champ: Optional[Champion]) -> bool:
        try:
            self.hexes[pos.y][pos.x] = champ
            return True
        except:
            return False

    def is_hex_empty(self, pos: Offset) -> Optional[bool]:
        if not self.is_position_valid(pos):
            return None
        return self.get(pos) == None

    def is_position_valid(self, pos: Point) -> bool:
        pos = offset(pos)
        return 0 <= pos.x and pos.x < self.width and 0 <= pos.y and pos.y < self.height
