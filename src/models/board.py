from typing import List

import constants

from champion import Champion


class Board:
  hexes: List[List[Champion or None]]

  def __init__(self):
    self.hexes = [[None for i in range(constants.BOARD_WIDTH)] for j in range(constants.BOARD_HEIGHT)]
