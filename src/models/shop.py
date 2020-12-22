from typing import List, Union

from champion import Champion
from player import Player
from pool import Pool


class Shop:
    """Per-player container of 5 rotating champ choices."""

    champs: List[Union[Champion, None]]
    is_locked: bool
    player: Player
    pool: Pool

    def __init__(self, player: Player):
        self.champs = []
        self.is_locked = False
        self.player = player

    def refresh(self):
        """Refresh shop choices unless it is locked."""
        if self.is_locked:
            self.is_locked = False
            return

        self.__flush()
        while len(self.champs) < 5:
            new_champ = self.pool.get(self.player)
            if new_champ:
                self.champs.append(new_champ)

    def pick(self, index: int) -> Union[Champion, None]:
        """Pick specified champ from shop."""
        champ = self.champs[index]
        self.champs[index] = None
        return champ

    def __flush(self):
        """Flush all remaining champs in this shop to the pool."""
        for champ in self.champs:
            if champ:
                self.pool.put(champ)
        self.champs = []
