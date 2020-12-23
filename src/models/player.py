from typing import Type

from constants import COST_REROLL

from bench import Bench
from board import Board
from champion import Champion
from pool import Pool
from shop import Shop


class Player:
    bench: Bench
    board: Board
    experience: int = 0
    gold: int = 0
    has_chosen: bool
    health: int = 100
    level: int = 1
    name: str
    shop: Shop
    pool: Pool

    def __init__(self, name: str, pool: Pool):
        self.board = Board(self)
        self.bench = Bench(self)
        self.experience = 0
        self.gold = 0
        self.has_chosen = False
        self.health = 100
        self.name = name
        self.pool = pool
        self.shop = Shop(self, pool)

    def reroll(self) -> bool:
        """Refresh shop if player can afford to. Returns whether reroll was successful or not."""
        if self.gold < COST_REROLL:
            return False

        self.gold -= COST_REROLL
        self.shop.refresh(True)
        return True

    def buy_champ(self, index: int):
        champ = self.shop.get(index)
        if not champ or self.bench.is_full() or self.gold < champ.cost:
            return None
        self.gold -= champ.cost
        self.shop.remove(index)
        self.bench.add_champ(champ)
