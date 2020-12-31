from typing import List, TypedDict


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
