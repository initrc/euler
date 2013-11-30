#!/usr/bin/env python

import math
from util.benchmark import benchmark

problem = "3. Largest prime factor"
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def solve():
    """Largest prime factor"""
    x = 600851475143
    factor, maxfactor = 2, 2
    # x has at most one factor that is greater than sqrt(x)
    gate = int(math.sqrt(x))
    while factor <= gate:
        if not x % factor:
            x //= factor
            maxfactor = factor
        else:
            factor += 1
    return maxfactor if x == 1 else x

if __name__ == '__main__':
    benchmark(problem, solve)
