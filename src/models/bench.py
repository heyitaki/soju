from typing import List

from constants import BENCH_SIZE

from board import Board
from champion import Champion
from item import Item
from player import Player


class Bench:
    items: List[Item]
    champs: List[Champion]
    player: Player

    def __init__(self, player: Player):
        self.champs = []
        self.items = []
        self.player = player

    def add_champ(self, champ: Champion):
        if not self.is_full():
            self.champs.append(champ)
        else:
            self.player.board.add_champ(champ)

    def is_full(self):
        return len(self.champs) == BENCH_SIZE
