from typing import Any, List, Union, cast

from src.constants import BOARD_HEIGHT, BOARD_WIDTH

from src.models.champion import Champion
from src.models.helpers.point import Point
from src.models.player import Player


class Board:
    """Hexagonal grid representing a player's half of the full field."""

    num_champs: int
    hexes: List[List[Union[Champion, None]]]
    player: Player

    def __init__(self, player: Player):
        self.hexes = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.player = player
        self.num_champs = 0

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
                self.__set(pos, champ)
                return True
            return False
        else:
            # Swap champs and return swapped champ
            champ_to_bench = cast(Champion, self.get_champ(pos))
            self.hexes[pos.y][pos.x] = champ
            return champ_to_bench

    def get_champ(self, pos: Point) -> Union[Champion, None]:
        try:
            return self.hexes[pos.y][pos.x]
        except:
            return None

    def is_full(self) -> bool:
        return self.num_champs >= self.player.max_champs

    def is_hex_empty(self, pos: Point) -> Union[bool, None]:
        if not pos.is_valid():
            return None
        return self.get_champ(pos) == None

    def move_champ(self, start_pos: Point, end_pos: Point) -> bool:
        """
        Move a champ on this board to a different position. Returns whether or not move was valid.
        """
        if (
            not start_pos.is_valid()
            or not end_pos.is_valid()
            or start_pos.is_equal(end_pos)
        ):
            return False

        champ1 = self.get_champ(start_pos)
        champ2 = self.get_champ(end_pos)
        if not champ1:
            return False
        elif champ2:
            # Swap champs
            self.__set(start_pos, champ2)
            self.__set(end_pos, champ1)
        else:
            # Place champ
            self.__set(start_pos, None)
            self.__set(end_pos, champ1)
        return True

    def remove_champ(self, pos: Point) -> Union[Champion, None]:
        if not pos.is_valid():
            return None

        champ = self.get_champ(pos)
        if champ:
            self.__set(pos, None)
            self.num_champs -= 1
            return champ
        return None

    def __set(self, pos: Point, champ: Union[Champion, None]) -> bool:
        try:
            self.hexes[pos.y][pos.x] = champ
            return True
        except:
            return False

    def __get_free_hex(self) -> Union[Point, None]:
        for y in reversed(range(BOARD_HEIGHT)):
            for x in range(BOARD_WIDTH):
                pos = Point(x, y)
                if self.is_hex_empty(pos):
                    return pos
        return None
