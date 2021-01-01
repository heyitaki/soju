from typing import List, TypedDict


class StatsData(TypedDict):
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


class ChampStatsData(TypedDict):
    armor: float
    attack_damage: float
    attack_speed: float
    health: float
    magic_resist: float
    mana: float
    mana_start: float
    range: float


class ChampData(TypedDict):
    name: str
    stats: ChampStatsData
    cost: int
    traits: List[str]


ChampDataList = List[ChampData]
