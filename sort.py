from enum import Enum, auto
from typing import List

class Ordering(Enum):
    LT = auto()
    EQ = auto()
    GT = auto()

class IntComparison(Enum):
    Natural = auto()
    Reverse = auto()
    Parity = auto()

def apply(cmp: IntComparison, x: int, y: int) -> Ordering:
    if cmp == IntComparison.Natural:
        if x < y:
            return Ordering.LT
        if x > y:
            return Ordering.GT
        return Ordering.EQ
    if cmp == IntComparison.Reverse:
        if x < y:
            return Ordering.GT
        if x > y:
            return Ordering.LT
        return Ordering.EQ
    if cmp == IntComparison.Parity:
        if x % 2 == y % 2:
            return Ordering.EQ
        if x % 2 == 0:
            return Ordering.LT
        return Ordering.GT

def sort(cmp: IntComparison, l: List[int]) -> List[int]:
    if len(l) == 0:
        return l
    x = l[0]
    lowers = sort(cmp, [y for y in l[1:] if apply(cmp, y, x) == Ordering.LT])
    uppers = sort(cmp, [y for y in l[1:] if apply(cmp, y, x) != Ordering.LT])
    result = []
    result += lowers
    result.append(x)
    result += uppers
    return result
