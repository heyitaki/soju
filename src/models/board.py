from typing import List, Union

import constants

from champion import Champion


class Board:
    hexes: List[List[Union[Champion, None]]]

    def __init__(self):
        self.hexes = [
            [None for _ in range(constants.BOARD_WIDTH)]
            for _ in range(constants.BOARD_HEIGHT)
        ]
