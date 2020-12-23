from typing import List, Union

from constants import BOARD_HEIGHT, BOARD_WIDTH

from champion import Champion
from player import Player


class Board:
    """Hexagonal grid representing a player's half of the full field."""

    hexes: List[List[Union[Champion, None]]]
    player: Player

    def __init__(self, player: Player):
        self.hexes = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.player = player

    def add_champ(self, champ: Champion):
        pass

    def sell(self, x: int, y: int):
        pass
