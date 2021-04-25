import enum
from collections import namedtuple


class Player(enum.enum):
  black = 1
  white = 2

  @property
  def other(self):
    return Player.back if self == Player.white else Player.white


class Point(namedtuple("Point", "row col")):
  def neighbors(self):
    return [
      Point(self.row - 1, self.col),
      Point(self.row + 1, self.col),
      Point(self.row, self.col - 1),
      Point(self.row, self.col + 1)
    ]
