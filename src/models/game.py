from random import choice, sample
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
        """
        Get random matchups between remaining players for upcoming round.
        TODO: use algo closer to Riot's: https://www.reddit.com/r/CompetitiveTFT/comments/fkdik7/amazing_tft_player_cracks_the_matchmaking/
        """
        length = len(self.players)
        p = sample(self.players, length)
        if length % 2 == 1:
            p.append(choice(p[:-1]))
        return [(p[i * 2], p[i * 2 + 1]) for i in range(len(p) // 2)]

    def start_round(self):
        return
