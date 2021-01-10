from typing import Union

from src.models.points.cube_point import CubePoint as Cube
from src.models.points.offset_point import OffsetPoint as Offset

Point = Union[Offset, Cube]
