from typing import TYPE_CHECKING, List, Optional, Tuple, Union

from src.constants import BOARD_HEIGHT, BOARD_WIDTH
from src.models.boards.hex_board import HexBoard

if TYPE_CHECKING:
    from src.models.champion import Champion
    from src.models.player import Player
    from src.models.points.offset_point import OffsetPoint


class RoundBoard(HexBoard):
    playerHome: Player
    playerAway: Player

    def __init__(self, players: Tuple[Player, Player]):
        super().__init__(BOARD_WIDTH, BOARD_HEIGHT * 2)
        self.playerHome, self.playerAway = players
        self.setup_hexes()

    def setup_hexes(self):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                pos = OffsetPoint(x, y)
                posA = self.translate_point(pos)
                self.set(pos, self.playerHome.board.get(pos))
                self.set(posA, self.playerAway.board.get(pos))

    def translate_point(self, pos: OffsetPoint) -> OffsetPoint:
        return OffsetPoint(self.width - pos.x, self.height - pos.y)
