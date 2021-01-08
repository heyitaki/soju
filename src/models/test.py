from copy import copy

from src.constants import BOARD_HEIGHT, BOARD_WIDTH
from src.models.boards.board import Board
from src.models.points.offset_point import OffsetPoint

# # Are changes to class variables shared across instances? A: NO
# class Dog:
#     kind = "canine"

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Dog(kind={self.kind}, name={self.name})"


# d1 = Dog("macy")
# d2 = Dog("hello")

# d1.kind = "porcupine"
# print(d1, d2)

# # Test offset -> cube
# b = Board(BOARD_WIDTH, BOARD_HEIGHT)
# points = [
#     OffsetPoint(0, 0),
#     OffsetPoint(0, 4),
#     OffsetPoint(0, 8),
#     OffsetPoint(0, 0),
#     OffsetPoint(3, 0),
#     OffsetPoint(3, 8),
# ]

# [print(x.to_cube()) for x in points]


# a = [1, 2, 3]
# b = copy(a)
# b[0] = 5
# print(a, b)


# class t:
#     def __init__(self):
#         self.t = 1


# a = [t(), t(), t()]
# print(a.index(a[1]))
