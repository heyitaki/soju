from typing import List, Tuple, Union

from constants import BOARD_HEIGHT, BOARD_WIDTH

from champion import Champion
from player import Player


class Field:
    playerHome: Player
    playerAway: Player
    hexes: List[List[Union[Champion, None]]]

    def __init__(self, players: Tuple[Player, Player]):
        self.hexes = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.playerHome, self.playerAway = players
