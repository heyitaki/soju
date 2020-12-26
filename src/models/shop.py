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

    def __init__(self, player: Player, pool: Pool):
        self.champs = []
        self.is_locked = False
        self.player = player
        self.pool = pool

    def refresh(self, player_triggered=False):
        """Refresh shop choices unless it is locked."""
        if player_triggered:
            self.is_locked = False

        if self.is_locked:
            self.is_locked = False
            return

        self.__flush()
        while len(self.champs) < 5:
            new_champ = self.pool.get(self.player.level)
            if new_champ:
                self.champs.append(new_champ)

    def get_champ(self, index: int) -> Union[Champion, None]:
        """Get specified champ from shop."""
        if not 0 <= index or not index < len(self.champs):
            return None
        return self.champs[index]

    def remove(self, index: int) -> None:
        """Remove specified champ from shop."""
        if 0 <= index and index < len(self.champs):
            self.champs[index] = None

    def __flush(self):
        """Flush all remaining champs in this shop to the pool."""
        for champ in self.champs:
            if champ:
                self.pool.put(champ)
        self.champs = []
