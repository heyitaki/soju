import random
from typing import Dict, List

from constants import CHAMP_DROP_RATE, CHAMP_POOL_SIZE

from champion import Champion
from player import Player


class Pool:
  champs: Dict[str, int] # Name of champ -> # left

  def __init__(self, champ_stats):
    self.champs = dict()
    for champ in champ_stats:
      self.champs[champ.name] = CHAMP_POOL_SIZE[champ.cost]
  

  def get(self, player: Player):
    '''
    Get random champ from pool according to champ drop & player level probabilities.
    '''
    rates = CHAMP_DROP_RATE[player.level]
    rand = random.random()

    # Get champ cost
    for j in range(0, len(rates)):
      rand -= rates[j]
      if (rand <= 0):
        champ_cost = j
        break
    
    # Get random champ with this cost

      


  def put(self, champs: List[Champion]) -> None:
    pass
