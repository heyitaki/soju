import math
import random
from types.champ_stats import ChampDataList
from typing import Dict, List, Sequence, Tuple, Union

from constants import CHAMP_DROP_RATE, CHAMP_POOL_SIZE

from champion import Champion
from player import Player


class Pool:
    # Champ cost -> [(Champ name, # left), ...]
    cost_to_counts: Dict[int, List[Tuple[Champion, int]]]

    def __init__(self, champ_data_list: ChampDataList):
        self.cost_to_counts = dict()
        for champ_data in champ_data_list:
            champ = Champion(champ_data)
            if champ.cost in self.cost_to_counts:
                self.cost_to_counts[champ.cost] = []
            self.cost_to_counts[champ.cost].append((champ, CHAMP_POOL_SIZE[champ.cost]))

    def get(self, player: Player) -> Union[Champion, None]:
        """Get random champ from pool according to champ drop & player level probabilities."""
        rates = CHAMP_DROP_RATE[player.level]

        # Get champ cost
        champ_cost = choose_rand_from_list(rates)
        if champ_cost == -1:
            return None

        # Get random champ with this cost
        champ_list = self.cost_to_counts[champ_cost]
        champ_counts: List[int] = [count for (_, count) in champ_list]
        champ_idx = choose_rand_from_list(champ_counts)
        if champ_idx == -1:
            return None
        champ_tuple = champ_list[champ_idx]

        # Update count and return Champion
        if champ_tuple[1] <= 0:
            return self.get(player)
        champ_list[champ_idx] = (champ_tuple[0], champ_tuple[1] - 1)
        return champ_tuple[0]

    def put(self, champs: List[Champion]) -> None:
        for champ in champs:
            pass


def choose_rand_from_list(weighted_list: Sequence[Union[int, float]]):
    """Choose a random index weighted by the values at each index of the given list."""
    total = sum(weighted_list)
    rand = random.uniform(0, total)
    for i in range(len(weighted_list)):
        rand -= weighted_list[i]
        if rand <= 0:
            return i
    return -1
