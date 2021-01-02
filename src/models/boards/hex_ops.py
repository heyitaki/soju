from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from src.models.champion import Champion
from src.models.helpers.point import Point

if TYPE_CHECKING:
    from src.models.boards.board import Board


def get_neighbors(board: Board, pos: Point) -> List[Point]:
    offset = 1 if pos.y % 2 == 0 else 0
    neighbors = [
        Point(pos.x + offset, pos.y + 1),
        Point(pos.x + offset + 1, pos.y + 1),
        Point(pos.x - 1, pos.y),
        Point(pos.x + 1, pos.y),
        Point(pos.x + offset, pos.y - 1),
        Point(pos.x + offset + 1, pos.y - 1),
    ]
    return list(filter(lambda pos: board.is_position_valid(pos), neighbors))


def get_closest_enemy(board: Board, pos: Point) -> Optional[Champion]:
    visited = set()
    queue = [pos]

    try:
        owner_id = board.get(pos).owner.id
    except:
        return None

    while len(queue) > 0 and not len(visited) == board.height * board.width:
        curr_pos = queue.pop(0)
        if not curr_pos in visited:
            champ = board.get(curr_pos)
            if champ and not champ.owner.id == owner_id:
                return champ
            visited.add(curr_pos)
            queue.extend(get_neighbors(board, curr_pos))
    return None
