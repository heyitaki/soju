from typing import List

from item import Item
from stats import Stats


class Champion:
  chosen_trait: str or None
  cost: int
  items: List[Item]
  level: int
  name: str
  stats: Stats
  stats_base: Stats
  traits: List[str]

