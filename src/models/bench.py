from typing import List, Union

from src.constants import BENCH_SIZE

from src.models.board import Board
from src.models.champion import Champion
from src.models.item import Item
from src.models.player import Player


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

    def get_champ(self, index: int):
        try:
            return self.champs[index]
        except:
            return None

    def is_full(self):
        return len(self.champs) == BENCH_SIZE

    def remove_champ(self, index: int) -> Union[Champion, None]:
        if 0 <= index and index < len(self.champs):
            return self.champs.pop(index)
        return None
