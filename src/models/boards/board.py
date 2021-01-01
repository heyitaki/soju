from typing import TYPE_CHECKING, List, Union

from src.models.helpers.point import Point

if TYPE_CHECKING:
    from src.models.champion import Champion


class Board:
    height: int
    hexes: List[List[Union[Champion, None]]]
    width: int

    def __init__(self, width: int, height: int):
        self.hexes = [[None for _ in range(width)] for _ in range(height)]

    def get(self, pos: Point) -> Union[Champion, None]:
        try:
            return self.hexes[pos.y][pos.x]
        except:
            return None

    def set(self, pos: Point, champ: Union[Champion, None]) -> bool:
        try:
            self.hexes[pos.y][pos.x] = champ
            return True
        except:
            return False

    def is_hex_empty(self, pos: Point) -> Union[bool, None]:
        if not self.is_position_valid(pos):
            return None
        return self.get(pos) == None

    def is_position_valid(self, pos: Point) -> bool:
        return 0 <= pos.x and pos.x < self.width and 0 <= pos.y and pos.y < self.height
