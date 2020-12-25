from __future__ import annotations

from copy import copy, deepcopy
from types.champ_stats import ChampData, ChampStatsData
from typing import List, Union

from item import Item


class Champion:
    chosen_trait: Union[str, None]
    cost: int
    id: int
    items: List[Item]
    level: int
    name: str
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


class ChampStats:
    ability_power: float
    armor: float
    attack_damage: float
    attack_speed: float
    crit_chance: float
    crit_modifier: float
    dodge: float
    health: float
    magic_resist: float
    mana: int
    mana_start: int
    range: int

    def __init__(self, stats: ChampStatsData):
        self.armor = stats["armor"]
        self.attack_damage = stats["attack_damage"]
        self.attack_speed = stats["attack_speed"]
        self.health = stats["health"]
        self.magic_resist = stats["magic_resist"]
        self.mana = int(stats["mana"])
        self.mana_start = int(stats["mana_start"])
        self.range = int(stats["range"])
        self.ability_power = 1.0
        self.crit_chance = 0.25
        self.crit_modifier = 1.5
        self.dodge = 0
