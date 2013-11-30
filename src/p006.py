#!/usr/bin/env python

from util.benchmark import benchmark

problem = "6. Sum square difference"
"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def solve():
    """Sum square difference"""
    nums = range(1, 101)
    return sum(nums) ** 2 - sum([x ** 2 for x in nums])

if __name__ == '__main__':
    benchmark(problem, solve)
