from typing import Type

from constants import COST_REROLL

from bench import Bench
from board import Board
from champion import Champion
from helpers.gold import get_sell_cost
from helpers.point import Point
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

    def bench_champ(self, board_pos: Point, bench_index: int = None) -> bool:
        """Move champ from board to bench if possible."""
        champ1 = self.board.get_champ(board_pos)
        if champ1:
            if not bench_index == None and (
                champ2 := self.bench.get_champ(bench_index)
            ):
                # Swap champs
                self.board.remove_champ(board_pos)
                self.bench.remove_champ(bench_index)
                self.board.add_champ(champ2, board_pos)
                self.bench.add_champ(champ1)
                return True
            elif not self.bench.is_full():
                # Add to bench
                self.board.remove_champ(board_pos)
                self.bench.add_champ(champ1)
                return True
        return False

    def buy_champ(self, shop_index: int) -> bool:
        """Buy champ from shop if player can afford to."""
        champ = self.shop.get_champ(shop_index)
        if not champ or self.bench.is_full() or self.gold < champ.cost:
            return False
        self.gold -= champ.cost
        self.shop.remove(shop_index)
        self.bench.add_champ(champ)
        return True

    def move_champ(self, start_pos: Point, end_pos: Point) -> bool:
        """Move a champ on the board to a different position."""
        return self.board.move_champ(start_pos, end_pos)

    def reroll(self) -> bool:
        """Refresh shop if player can afford to."""
        if self.gold < COST_REROLL:
            return False
        self.gold -= COST_REROLL
        self.shop.refresh(True)
        return True

    def sell_champ_from_bench(self, index: int) -> bool:
        """As self explanatory as it gets."""
        champ = self.bench.remove_champ(index)
        if champ:
            self.pool.put(champ)
            self.gold += get_sell_cost(champ)
            return True
        return False

    def sell_champ_from_board(self, pos: Point) -> bool:
        """Deja vu?"""
        champ = self.board.remove_champ(pos)
        if champ:
            self.pool.put(champ)
            self.gold += get_sell_cost(champ)
            return True
        return False

    def unbench_champ(self, bench_index: int, board_pos: Point):
        """Move champ from bench to board if possible."""
        champ1 = self.bench.get_champ(bench_index)
        champ2 = self.board.get_champ(board_pos)
        if champ1:
            if champ2:
                # Swap champs
                self.board.remove_champ(board_pos)
                self.bench.remove_champ(bench_index)
                self.board.add_champ(champ2, board_pos)
                self.bench.add_champ(champ1)
                return True
            elif not self.board.is_full():
                # Add to board
                self.bench.remove_champ(bench_index)
                self.board.add_champ(champ1, board_pos)
                return True
        return False
