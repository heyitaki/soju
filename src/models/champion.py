from __future__ import annotations

from copy import copy, deepcopy
from types.champ_stats import StatsData
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
    traits: List[str]

    def __init__(self, champ_data: ChampData):
        self.chosen_trait = None
        self.cost = champ_data["cost"]
        self.id = 0
        self.items = []
        self.level = 1
        self.name = champ_data["name"]
        self.stats = ChampStats(champ_data["stats"])
        self.traits = champ_data["traits"]

    def clone(self, id: int, chosen_trait: str = None, item: Item = None) -> Champion:
        """
        Create a copy of this champ with specified chosen trait, item, and id.
        TODO: when implementing items + chosen, need to remove traits given by spat items
        """
        new_champ = deepcopy(self)
        new_champ.id = id
        new_champ.level = 2 if chosen_trait else 1
        new_champ.chosen_trait = chosen_trait
        new_champ.items = [item] if item else []
        new_champ.stats.reset()
        return new_champ

    def get_sell_cost(self) -> int:
        if self.level == 1:
            return self.cost
        else:
            return self.cost - 1


class ChampStats:
    base: Stats
    current: Stats

    def __init__(self, stats: ChampStatsData):
        self.base = Stats.from_champ_stats_data(stats)
        self.reset()

    def reset(self):
        self.current = copy(self.base)


class Stats:
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

    def __init__(self, data: StatsData):
        self.ability_power = data["ability_power"]
        self.armor = data["armor"]
        self.attack_damage = data["attack_damage"]
        self.attack_speed = data["attack_speed"]
        self.crit_chance = data["crit_chance"]
        self.crit_modifier = data["crit_modifier"]
        self.dodge = data["dodge"]
        self.health = data["health"]
        self.magic_resist = data["magic_resist"]
        self.mana = data["mana"]
        self.mana_start = data["mana_start"]
        self.range = data["range"]

    @classmethod
    def from_champ_stats_data(cls, data: ChampStatsData) -> Stats:
        return cls(
            {
                "ability_power": 1.0,
                "armor": data["armor"],
                "attack_damage": data["attack_damage"],
                "attack_speed": data["attack_speed"],
                "crit_chance": 0.25,
                "crit_modifier": 1.5,
                "dodge": 0,
                "health": data["health"],
                "magic_resist": data["magic_resist"],
                "mana": int(data["mana"]),
                "mana_start": int(data["mana_start"]),
                "range": int(data["range"]),
            }
        )
