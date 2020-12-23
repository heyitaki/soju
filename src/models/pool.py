import logging
from random import uniform
from types.champ_stats import ChampDataList
from typing import Dict, List, Sequence, Tuple, Union

from constants import CHAMP_DROP_RATE, CHAMP_POOL_SIZE

from champion import Champion


class Pool:
    """Container for all champions unacquired by players."""

    # {Champ cost: {Champ name: # left}}
    cost_to_counts: Dict[int, Dict[str, int]]
    # {Champ name: Champ}
    name_to_champ: Dict[str, Champion]

    def __init__(self, champ_data_list: ChampDataList):
        self.cost_to_counts = dict()
        self.name_to_champ = dict()
        for champ_data in champ_data_list:
            champ = Champion(champ_data)
            self.cost_to_counts[champ.cost][champ.name] = CHAMP_POOL_SIZE[champ.cost]
            self.name_to_champ[champ.name] = champ

    def get(self, player_level: int) -> Union[Champion, None]:
        """Get random champ from pool according to champ drop & player level probabilities."""
        rates = CHAMP_DROP_RATE[player_level]

        # Get champ cost
        champ_cost = choose_rand_from_list(rates)
        if champ_cost == -1:
            logging.error("Failed to select random champ cost.")
            return None

        # Get random champ with this cost
        name_to_counts = self.cost_to_counts[champ_cost]
        name_count_tuples = [(name, name_to_counts[name]) for name in name_to_counts]
        champ_counts = [count for (_, count) in name_count_tuples]
        champ_idx = choose_rand_from_list(champ_counts)
        if champ_idx == -1:
            logging.error("Failed to select random champion.")
            return None
        champ_tuple = name_count_tuples[champ_idx]

        # Update count and return Champion
        if champ_tuple[1] <= 0:
            return self.get(player_level)
        name_to_counts[champ_tuple[0]] = champ_tuple[1] - 1
        return self.name_to_champ[champ_tuple[0]].clone()

    def put(self, champ: Champion) -> None:
        """Introduce champ back to this pool."""
        self.cost_to_counts[champ.cost][champ.name] += 1


def choose_rand_from_list(weighted_list: Sequence[Union[int, float]]):
    """Choose a random index weighted by the values at each index of the given list."""
    total = sum(weighted_list)
    rand = uniform(0, total)
    for i in range(len(weighted_list)):
        rand -= weighted_list[i]
        if rand <= 0:
            return i
    return -1
