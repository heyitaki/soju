from typing import List

from constants import NUM_PLAYERS
from load import load_champ_data

from player import Player
from pool import Pool


class Game:
    round: int
    players: List[Player]
    pool: Pool

    def __init__(self):
        self.pool = Pool(load_champ_data())
        self.round = 0
        self.players = [Player(str(i), self.pool) for i in range(NUM_PLAYERS)]
