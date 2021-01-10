from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

from src.models.points.cube_point import CubePoint as Cube
from src.models.points.offset_point import OffsetPoint as Offset
from src.models.points.offset_point import offset
from src.models.points.point import Point

if TYPE_CHECKING:
    from src.models.champion import Champion


class ChampBoard:
    height: int
    champs: Dict[Offset, Champion]  # {start_pos: champ}
    width: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.champs = {}

    def get(self, pos: Point) -> Optional[Champion]:
        pos = offset(pos)
        try:
            return self.champs[pos]
        except:
            return None

    def get_champs(self):
        return list(self.champs.values())

    def get_points(self):
        return list(self.champs.keys())

    def is_hex_empty(self, pos: Offset) -> Optional[bool]:
        if not self.is_position_valid(pos):
            return None
        return self.get(pos) == None

    def is_position_valid(self, pos: Point) -> bool:
        pos = offset(pos)
        return 0 <= pos.x and pos.x < self.width and 0 <= pos.y and pos.y < self.height

    def set(self, pos: Point, champ: Optional[Champion]) -> bool:
        pos = offset(pos)
        try:
            if champ is None:
                self.champs.pop(pos)
            else:
                self.champs[pos] = champ
            return True
        except:
            return False
