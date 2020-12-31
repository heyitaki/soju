from typing import List, Union

from champion import Champion
from helpers.point import Point


class Board:
    hexes: List[List[Union[Champion, None]]]

    def __init__(self, width: int, height: int):
        self.hexes = [[None for _ in range(width)] for _ in range(height)]

    def get(self, pos: Point):
        