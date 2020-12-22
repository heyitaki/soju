from typing import List, Union

from champion import Champion

# import constants



class Board:
  hexes: List[List[Union[Champion, None]]]

  def __init__(self):
    self.hexes = [[None for _ in range(4)] for _ in range(7)]

b= Board()
print(len(b.hexes), len(b.hexes[0]))
