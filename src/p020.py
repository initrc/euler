#!/usr/bin/env python

import math
from util.benchmark import benchmark

problem = "20. Factorial digit sum"
"""
n! means n x (n − 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def solve():
    """Factorial digit sum"""
    x = math.factorial(100)
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

if __name__ == '__main__':
    benchmark(problem, solve)
