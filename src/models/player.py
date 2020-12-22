from typing import Type

from bench import Bench
from board import Board
from shop import Shop


class Player:
    bench: Type[Bench]
    board: Type[Board]
    experience: int = 0
    gold: int = 0
    has_chosen: bool
    health: int = 100
    level: int = 1
    name: str
    shop: Type[Shop]
