#!/usr/bin/env python

from util.benchmark import benchmark
from util.prime import primeset

problem = "10. Summation of primes"
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def solve():
    """Summation of primes"""
    return sum(primeset(2000000))

if __name__ == '__main__':
    benchmark(problem, solve)
