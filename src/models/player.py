from typing import Type

from constants import COST_REROLL

from bench import Bench
from board import Board
from champion import Champion
from pool import Pool
from shop import Shop


class Player:
    """Container for all player-specific state. Represents a player in a game."""

    bench: Bench
    board: Board
    experience: int
    gold: int
    has_chosen: bool
    health: int
    level: int
    max_champs: int  # Can be different from level because of FON
    name: str
    pool: Pool
    shop: Shop

    def __init__(self, name: str, pool: Pool):
        self.board = Board(self)
        self.bench = Bench(self)
        self.experience = 0
        self.gold = 0
        self.has_chosen = False
        self.health = 100
        self.level = 1
        self.max_champs = 1
        self.name = name
        self.pool = pool
        self.shop = Shop(self, pool)

    def reroll(self) -> bool:
        """Refresh shop if player can afford to. Returns whether reroll was successful."""
        if self.gold < COST_REROLL:
            return False
        self.gold -= COST_REROLL
        self.shop.refresh(True)
        return True

    def buy_champ(self, index: int):
        """Buy champ from shop if player can afford to. Returns whether purchase was successful."""
        champ = self.shop.get(index)
        if not champ or self.bench.is_full() or self.gold < champ.cost:
            return False
        self.gold -= champ.cost
        self.shop.remove(index)
        self.bench.add_champ(champ)
        return True
