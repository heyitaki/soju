from typing import Any, List, Union, cast

from constants import BOARD_HEIGHT, BOARD_WIDTH

from champion import Champion
from helpers.point import Point
from player import Player


class Board:
    """Hexagonal grid representing a player's half of the full field."""

    num_champs: int
    num_pets: int
    hexes: List[List[Union[Champion, None]]]
    player: Player

    def __init__(self, player: Player):
        self.hexes = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.player = player
        self.num_champs = 0
        self.num_pets = 0

    def add_champ(self, champ: Champion, pos: Point) -> Union[bool, Champion]:
        if not pos:
            # Only time we're adding a champ without a specified position is from carousel while
            # player has a full bench
            new_pos = self.__get_free_hex()
            if new_pos:
                self.num_champs += 1
                self.hexes[new_pos.y][new_pos.x] = champ
                return True
            return False
        elif not pos.is_valid():
            # Make sure given position is valid
            return False
        elif self.is_hex_empty(pos):
            # Place champ on board
            if self.num_champs < self.player.max_champs:
                self.num_champs += 1
                self.hexes[pos.y][pos.x] = champ
                return True
            return False
        else:
            # Swap champs and return swapped champ
            champ_to_bench = cast(Champion, self.hexes[pos.y][pos.x])
            self.hexes[pos.y][pos.x] = champ
            return champ_to_bench

    def is_full(self):
        return self.num_champs >= self.player.max_champs

    def is_hex_empty(self, pos: Point) -> Union[bool, None]:
        if not pos.is_valid():
            return None
        return self.hexes[pos.y][pos.x] == None

    def move_champ(self, pos1: Point, pos2: Point):
        pass

    def remove_champ(self, champ: Champion):
        pass

    def sell(self, pos: Point):
        pass

    def __get_free_hex(self) -> Union[Point, None]:
        for y in reversed(range(BOARD_HEIGHT)):
            for x in range(BOARD_WIDTH):
                pos = Point(x, y)
                if self.is_hex_empty(pos):
                    return pos
        return None
