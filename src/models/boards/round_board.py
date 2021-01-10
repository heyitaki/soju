from typing import TYPE_CHECKING, List, Optional, Tuple, Union, cast

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
        for pos, champ in self.playerHome.board.champs.items():
            champ.setpos(pos)
            self.set(pos, champ)

        for pos, champ in self.playerAway.board.champs.items():
            pos = self.translate_point(pos)
            champ.setpos(pos)
            self.set(pos, champ)

    def translate_point(self, pos: OffsetPoint) -> OffsetPoint:
        return OffsetPoint(self.width - pos.x, self.height - pos.y)
