from typing import TYPE_CHECKING, List, Optional, Tuple, Union

from models.boards.board import Board
from src.constants import BOARD_HEIGHT, BOARD_WIDTH

if TYPE_CHECKING:
    from src.models.champion import Champion
    from src.models.helpers.point import Point
    from src.models.player import Player


class RoundBoard(Board):
    playerHome: Player
    playerAway: Player

    def __init__(self, players: Tuple[Player, Player]):
        super().__init__(BOARD_WIDTH, BOARD_HEIGHT * 2)
        self.playerHome, self.playerAway = players
        self.setup_hexes()

    def setup_hexes(self):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                pos = Point(x, y)
                posA = self.translate_point(pos)
                self.set(pos, self.playerHome.board.get(pos))
                self.set(posA, self.playerAway.board.get(pos))

    def translate_point(self, pos: Point) -> Point:
        return Point(self.width - pos.x, self.height - pos.y)
