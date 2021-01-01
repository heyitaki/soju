from typing import TYPE_CHECKING, List, Union, cast

from models.boards.board import Board
from src.constants import BOARD_HEIGHT, BOARD_WIDTH

if TYPE_CHECKING:
    from src.models.champion import Champion
    from src.models.helpers.point import Point
    from src.models.player import Player


class PlayerBoard(Board):
    """Hexagonal grid representing a player's half of the full field."""

    num_champs: int
    player: Player

    def __init__(self, player: Player):
        super().__init__(BOARD_WIDTH, BOARD_HEIGHT)
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
        elif not self.is_position_valid(pos):
            # Make sure given position is valid
            return False
        elif self.is_hex_empty(pos):
            # Place champ on board
            if self.num_champs < self.player.max_champs:
                self.num_champs += 1
                self.set(pos, champ)
                return True
            return False
        else:
            # Swap champs and return swapped champ
            champ_to_bench = cast(Champion, self.get(pos))
            self.hexes[pos.y][pos.x] = champ
            return champ_to_bench

    def is_full(self) -> bool:
        return self.num_champs >= self.player.max_champs

    def move_champ(self, start_pos: Point, end_pos: Point) -> bool:
        """
        Move a champ on this board to a different position. Returns whether or not move was valid.
        """
        if (
            not self.is_position_valid(start_pos)
            or not self.is_position_valid(end_pos)
            or start_pos.is_equal(end_pos)
        ):
            return False

        champ1 = self.get(start_pos)
        champ2 = self.get(end_pos)
        if not champ1:
            return False
        elif champ2:
            # Swap champs
            self.set(start_pos, champ2)
            self.set(end_pos, champ1)
        else:
            # Place champ
            self.set(start_pos, None)
            self.set(end_pos, champ1)
        return True

    def remove_champ(self, pos: Point) -> Union[Champion, None]:
        if not pos: #.is_valid():
            return None

        champ = self.get(pos)
        if champ:
            self.set(pos, None)
            self.num_champs -= 1
            return champ
        return None

    def __get_free_hex(self) -> Union[Point, None]:
        for y in reversed(range(BOARD_HEIGHT)):
            for x in range(BOARD_WIDTH):
                pos = Point(x, y)
                if self.is_hex_empty(pos):
                    return pos
        return None
