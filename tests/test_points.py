from src.models.points.cube_point import CubePoint
from src.models.points.offset_point import OffsetPoint


def test_round_trip():
    point = OffsetPoint(3, 0)
    assert point == point.to_cube()
    assert point == point.to_cube().to_offset()

    point = CubePoint(-5, -2, 7)
    assert point == point.to_offset()
    assert point == point.to_offset().to_cube()
