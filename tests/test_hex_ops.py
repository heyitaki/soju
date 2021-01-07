from src.models.points.offset_point import OffsetPoint


def test_get_neighbors(pos: OffsetPoint):
    pos = OffsetPoint(3, 5)
    offset = 1 if pos.y % 2 == 0 else 0
    neighbors = [
        OffsetPoint(pos.x + offset, pos.y + 1),
        OffsetPoint(pos.x + offset + 1, pos.y + 1),
        OffsetPoint(pos.x - 1, pos.y),
        OffsetPoint(pos.x + 1, pos.y),
        OffsetPoint(pos.x + offset, pos.y - 1),
        OffsetPoint(pos.x + offset + 1, pos.y - 1),
    ]
