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
        self.ability_power = 1.0
        self.armor = stats["armor"]
        self.attack_damage = stats["attack_damage"]
        self.attack_speed = stats["attack_speed"]
        self.crit_chance = 0.25
        self.crit_modifier = 1.5
        self.dodge = 0
        self.health = stats["health"]
        self.magic_resist = stats["magic_resist"]
        self.mana = int(stats["mana"])
        self.mana_start = int(stats["mana_start"])
        self.range = int(stats["range"])

    def toJSON(self) -> ChampStatsData:
        return {
            "armor": self.armor,
            "attack_damage": self.attack_damage,
            "attack_speed": self.attack_speed,
            "health": self.health,
            "magic_resist": self.magic_resist,
            "mana": self.mana,
            "mana_start": self.mana_start,
            "range": self.range,
        }
