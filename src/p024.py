#!/usr/bin/env python

import itertools
from functools import reduce
from util.benchmark import benchmark

problem = "24. Lexicographic permutations"
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def solve():
    """Lexicographic permutations"""
    LIMIT = 1000000
    p = itertools.permutations(range(10))
    for i in range(LIMIT - 1):
        next(p)
    return reduce(lambda x, y: x * 10 + y, next(p))

if __name__ == '__main__':
    benchmark(problem, solve)
