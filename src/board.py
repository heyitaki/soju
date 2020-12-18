import constants


class Board:
  def __init__(self):
    self.tiles = [
      [None for i in range(constants.BOARD_WIDTH)] for j in range(constants.BOARD_HEIGHT)
    ]
