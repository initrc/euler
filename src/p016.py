#!/usr/bin/env python

from util.benchmark import benchmark

problem = "16. Power digit sum"
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solve():
    """Power digit sum"""
    num = 2 ** 1000
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

if __name__ == '__main__':
    benchmark(problem, solve)
