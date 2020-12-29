from random import randrange
from typing import List, Tuple

from constants import NUM_PLAYERS
from load_data import load_champ_data

from helpers.result import Result
from player import Player
from pool import Pool


class Game:
    history: List[Tuple[int, Result]]  # [(Player id, win/loss)]
    players: List[Player]  # players + rankings = all players
    pool: Pool
    rankings: List[Player]
    round: int

    def __init__(self):
        self.pool = Pool(load_champ_data())
        self.rankings = []
        self.round = 0

        self.players = [Player(str(i), self.pool) for i in range(NUM_PLAYERS)]

    def get_matchups(self):
        matchups = []
        p = self.players.copy()
        while len(p) > 1:
            p1 = p.pop(randrange(len(p)))
            p2 = p.pop(randrange(len(p)))
            matchups.append((p1, p2))
        if len(p) > 0:
            matchups.append((p[0],))
