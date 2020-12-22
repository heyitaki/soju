from __future__ import annotations

from types.champ_stats import ChampData
from typing import List, Union

from item import Item
from stats import Stats
from copy import deepcopy, copy


class Champion:
    chosen_trait: Union[str, None]
    cost: int
    items: List[Item]
    level: int
    name: str
    stats: Stats
    stats_base: Stats
    traits: List[str]

    def __init__(self, champ_data: ChampData):
        self.chosen_trait = None
        self.cost = champ_data["cost"]
        self.items = []
        self.level = 1
        self.name = champ_data["name"]
        self.stats = Stats(champ_data["stats"])
        self.stats_base = Stats(champ_data["stats"])
        self.traits = champ_data["traits"]

    def clone(self, chosen_trait: str = None, item: Item = None) -> Champion:
        new_champ = deepcopy(self)
        new_champ.stats = copy(new_champ.stats_base)
        new_champ.level = 2 if chosen_trait else 1
        new_champ.chosen_trait = chosen_trait
        new_champ.items = [item] if item else []
        return new_champ
