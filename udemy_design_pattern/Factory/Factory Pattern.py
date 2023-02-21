from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __str__(self):
        return f"x: {self.x}, y : {self.y}"

    def __init__(self)
