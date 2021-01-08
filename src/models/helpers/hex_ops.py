from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from src.models.champion import Champion
from src.models.points.cube_point import CubePoint as Cube
from src.models.points.offset_point import OffsetPoint as Offset

if TYPE_CHECKING:
    from src.models.boards.board import Board

directions: List[Cube] = [
    Cube(1, 0, -1),  # NE
    Cube(0, 1, -1),  # NW
    Cube(-1, 1, 0),  # W
    Cube(-1, 0, 1),  # SW
    Cube(0, -1, 1),  # SE
    Cube(1, -1, 0),  # E
]


def get_neighbors(point: Union[Cube, Offset]) -> List[Cube]:
    return list(map(lambda dir: point + dir, directions))


def get_valid_points(board: Board, points: List[Union[Cube, Offset]]):
    return filter(lambda p: board.is_position_valid(p), points)


def get_n_closest_enemies(board: Board, point: Union[Cube, Offset]) -> List[Champion]:
    return []


# def get_closest_enemy(board: Board, pos: OffsetPoint) -> Optional[Champion]:
#     visited = set()
#     queue = [pos]

#     try:
#         owner_id = board.get(pos).owner.id
#     except:
#         return None

#     while len(queue) > 0 and not len(visited) == board.height * board.width:
#         curr_pos = queue.pop(0)
#         if not curr_pos in visited:
#             champ = board.get(curr_pos)
#             if champ and not champ.owner.id == owner_id:
#                 return champ
#             visited.add(curr_pos)
#             queue.extend(get_neighbors(board, curr_pos))
#     return None
