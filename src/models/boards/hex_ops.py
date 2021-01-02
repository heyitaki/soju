from typing import List

from src.models.boards.board import Board
from src.models.helpers.point import Point


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


def get_closest_enemy(board: Board, pos: Point) -> Point:
    visited = set()
    queue = [pos]
    while len(queue) > 0 and not len(visited) == board.height * board.width:
        curr_pos = queue.pop(0)
        if not curr_pos in visited:
            if not board.get(curr_pos) == None:
                
    return Point(0, 0)
