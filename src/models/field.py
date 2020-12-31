from typing import List, Tuple, Union

from src.constants import BOARD_HEIGHT, BOARD_WIDTH

from src.models.champion import Champion
from src.models.helpers.point import Point
from src.models.player import Player


class Field:
    playerHome: Player
    playerAway: Player
    hexes: List[List[Union[Champion, None]]]

    def __init__(self, players: Tuple[Player, Player]):
        self.hexes = [
            [None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT * 2)
        ]
        self.playerHome, self.playerAway = players

    def setup_hexes(self):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                self.hexes[y][x] = self.playerHome.board.get_champ(Point(x, y))

    # def __set(self, )
