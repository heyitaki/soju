from typing import Dict, List

from constants import CHAMP_POOL_SIZE

from champion import Champion
from player import Player


class Pool:
  champs: Dict[str, int] # Name of champ -> # left

  def __init__(self, champ_stats):
    self.champs = dict()
    for champ in champ_stats:
      self.champs[champ.name] = CHAMP_POOL_SIZE[champ.cost]
  
  def get5(self, player: Player) -> List:
    pass

  def put(self, champs: List[Champion]) -> None:
    pass
