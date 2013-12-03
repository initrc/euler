#!/usr/bin/env python

import math
from util.benchmark import benchmark

problem = "15. Lattice paths"
"""
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

rrdd, rdrd, rddr, drrd, drdr, ddrr

How many such routes are there through a 20x20 grid?
"""


def solve():
    """Lattice paths"""
    f = math.factorial
    nCr = lambda n, r: f(n) // f(r) // f(n - r)
    length = 20
    return nCr(length * 2, length)

if __name__ == '__main__':
    benchmark(problem, solve)
