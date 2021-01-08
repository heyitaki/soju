from __future__ import annotations

from typing import Final, List, Union

from src.models.points.cube_point import CubePoint as Cube
from src.models.points.offset_point import OffsetPoint as Offset

CUBE_DIRECTIONS: Final[List[Cube]] = [
    Cube(1, 0, -1),  # NE
    Cube(0, 1, -1),  # NW
    Cube(-1, 1, 0),  # W
    Cube(-1, 0, 1),  # SW
    Cube(0, -1, 1),  # SE
    Cube(1, -1, 0),  # E
]


def get_neighbors(point: Union[Cube, Offset]) -> List[Cube]:
    return list(map(lambda dir: point + dir, CUBE_DIRECTIONS))
