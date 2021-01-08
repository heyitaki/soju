from __future__ import annotations

from typing import List, Union

from src.models.points.cube_point import CubePoint as Cube
from src.models.points.offset_point import OffsetPoint as Offset


class Direction:
    NE = Cube(1, 0, -1)
    NW = Cube(0, 1, -1)
    W = Cube(-1, 1, 0)
    SW = Cube(-1, 0, 1)
    SE = Cube(0, -1, 1)
    E = Cube(1, -1, 0)

    @classmethod
    def getall(cls):
        return [cls.NE, cls.NW, cls.W, cls.SW, cls.SE, cls.E]


def get_neighbors(point: Union[Cube, Offset]) -> List[Cube]:
    return list(map(lambda dir: point + dir, Direction.getall()))


def get_neighbor(point: Union[Cube, Offset], direction: Cube) -> Cube:
    return point + direction


def get_points_from_ring(center: Union[Cube, Offset], radius: int):
    if isinstance(center, Offset):
        center = center.to_cube()
    if radius <= 0:
        return [center]

    points: List[Cube] = []
    start = center + Direction.SE * radius
    dirs = Direction.getall()
    for i in range(len(dirs)):
        for _ in range(radius):
            points.append(start)
            start += dirs[i]

    return points


def get_distance_euclidean(p1: Cube, p2: Cube):
    pass


def get_distance_manhattan(p1: Cube, p2: Cube):
    return (abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)) / 2
