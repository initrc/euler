#!/usr/bin/env python

import math
from util.benchmark import benchmark

problem = "9. Special Pythagorean triplet"
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solve():
    """Special Pythagorean triplet"""
    sum = 1000
    squares = set()
    for i in range(1, sum - 1):
        squares.add(i * i)
    for a in range(1, sum // 3):
        for b in range(a + 1, sum // 2):
            c2 = a*a + b*b
            if c2 in squares:
                c = int(math.sqrt(c2))
                if a + b + c == 1000:
                    return "a=%d, b=%d, c=%d, abc=%d" % (a, b, c, a*b*c)

if __name__ == '__main__':
    benchmark(problem, solve)
