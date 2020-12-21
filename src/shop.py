from typing import List

from champion import Champion
from player import Player


class Shop:
  champs: List[Champion]
  is_locked: bool
  player: Player

  def __init__(self, player: Player):
    self.player = player
