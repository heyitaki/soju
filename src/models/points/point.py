from typing import Union

import src.models.points.cube_point
import src.models.points.offset_point

Point = Union[
    src.models.points.offset_point.OffsetPoint, src.models.points.cube_point.CubePoint
]
