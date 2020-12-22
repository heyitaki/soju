from typing import List

from item import Item
from stats import Stats
from types.champ_stats import ChampData, ChampInfoList


class Champion:
    chosen_trait: str or None
    cost: int
    items: List[Item]
    level: int
    name: str
    stats: Stats
    stats_base: Stats
    traits: List[str]

    def __init__(self, champ_info: ChampData, chosen: bool, chosen_trait: str):
        self.name = champ_info.name
        self.cost = champ_info.cost
        self.
        self.level = 1 if chosen else 2
        
