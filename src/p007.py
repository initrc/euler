#!/usr/bin/env python

from util.benchmark import benchmark
from util.prime import isprime

problem = "7. 10001st prime"
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""


def solve():
    """10001st prime"""
    x = 3
    idx = 3
    while idx <= 10001:
        x += 2
        if isprime(x):
            idx += 1
    return x

if __name__ == '__main__':
    benchmark(problem, solve)
