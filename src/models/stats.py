from __future__ import annotations

from types.champ_stats import ChampStatsData


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
