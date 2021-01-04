from src.models.points.offset_point import OffsetPoint


def test_conversion():
    point = OffsetPoint(0, 0)
    assert point == point.to_cube()
    assert point == point.to_cube().to_offset()
