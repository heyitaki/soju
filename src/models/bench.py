from typing import List, Union

from constants import BENCH_SIZE

from board import Board
from champion import Champion
from item import Item
from player import Player


class Bench:
    """Container for all benched champs and items."""

    items: List[Item]
    champs: List[Champion]
    player: Player

    def __init__(self, player: Player):
        self.champs = []
        self.items = []
        self.player = player

    def add_champ(self, champ: Champion) -> Union[Champion, None]:
        if not self.is_full():
            self.champs.append(champ)
            return None
        return champ

    def is_full(self):
        return len(self.champs) == BENCH_SIZE

    def remove_champ(self, index: int) -> Union[Champion, None]:
        if 0 <= index and index < len(self.champs):
            return self.champs.pop(index)
        return None
