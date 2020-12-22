from __future__ import annotations

from types.champ_stats import ChampData
from typing import List, Union

from item import Item
from stats import Stats


class Champion:
    chosen_trait: Union[str, None]
    cost: int
    items: List[Item]
    level: int
    name: str
    stats: Stats
    stats_base: Stats
    traits: List[str]

    def __init__(
        self, champ_data: ChampData, chosen_trait: str = None, item: Item = None
    ):
        self.chosen_trait = chosen_trait
        self.cost = champ_data["cost"]
        self.items = [item] if item else []
        self.level = 1 if chosen_trait else 2
        self.name = champ_data["name"]
        self.stats = Stats(champ_data["stats"])
        self.stats_base = Stats(champ_data["stats"])
        self.traits = champ_data["traits"]

    def clone(self) -> Champion:
        return Champion(
            {
                "cost": self.cost,
                "name": self.name,
                "stats": self.stats.toJSON(),
                "traits": self.traits.copy(),
            }
        )
