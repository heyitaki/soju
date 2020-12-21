from typing import Type

from bench import Bench
from board import Board
from shop import Shop


class Player:
  health: int = 100
  name: str
  gold: int = 0
  board: Type[Board]
  bench: Type[Bench]
  level: int = 1
  shop: Type[Shop]