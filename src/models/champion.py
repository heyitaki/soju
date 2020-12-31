from __future__ import annotations

from copy import copy, deepcopy
from typing import TYPE_CHECKING, List, Union

from src.load_data import load_champ_data

if TYPE_CHECKING:
    from src.models.item import Item
    from src.models.player import Player
    from src.types.champ_stats import ChampData, ChampStatsData


class Champion:
    chosen_trait: Union[str, None]
    cost: int
    id: int
    items: List[Item]
    level: int
    name: str
    owner: Player
    stats: ChampStats
    stats_base: ChampStats
    traits: List[str]

    def __init__(self, champ_data: ChampData):
        self.chosen_trait = None
        self.cost = champ_data["cost"]
        self.id = 0
        self.items = []
        self.level = 1
        self.name = champ_data["name"]
        self.stats = ChampStats(champ_data["stats"])
        self.stats_base = ChampStats(champ_data["stats"])
        self.traits = champ_data["traits"]

    def clone(self, id: int, chosen_trait: str = None, item: Item = None) -> Champion:
        new_champ = deepcopy(self)
        new_champ.id = id
        new_champ.stats = copy(new_champ.stats_base)
        new_champ.level = 2 if chosen_trait else 1
        new_champ.chosen_trait = chosen_trait
        new_champ.items = [item] if item else []
        return new_champ

    def get_sell_cost(self) -> int:
        if self.level == 1:
            return self.cost
        else:
            return self.cost - 1


class ChampStats:
    ability_power: float
    armor: float
    attack_damage: float
    attack_speed: float
    base: ChampStats
    crit_chance: float
    crit_modifier: float
    dodge: float
    health: float
    magic_resist: float
    mana: int
    mana_start: int
    range: int

    def __init__(self, stats: ChampStatsData = None):
        if stats:
            self.base = ChampStats()
            self.base.ability_power = 1.0
            self.base.armor = stats["armor"]
            self.base.attack_damage = stats["attack_damage"]
            self.base.attack_speed = stats["attack_speed"]
            self.base.base = self.base
            self.base.crit_chance = 0.25
            self.base.crit_modifier = 1.5
            self.base.dodge = 0
            self.base.health = stats["health"]
            self.base.magic_resist = stats["magic_resist"]
            self.base.mana = int(stats["mana"])
            self.base.mana_start = int(stats["mana_start"])
            self.base.range = int(stats["range"])

    # def reset(self):


cs = ChampStats(load_champ_data()[0]["stats"])
# print([cs[k] for k in cs])
