#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util.benchmark import benchmark

problem = "14. Longest Collatz sequence"
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def solve():
    """Longest Collatz sequence"""
    f = lambda n: n // 2 if not n % 2 else 3 * n + 1
    history = {1: 1}
    maxchain, maxnum = 1, 1
    for num in range(999999, 0, -1):
        chain = []
        x = num
        while x not in history and x != 1:
            chain.insert(0, x)
            x = f(x)
        baselen = history[x]
        for idx, val in enumerate(chain):
            history[val] = baselen + idx + 1
        if history[num] > maxchain:
            maxchain = history[num]
            maxnum = num
    return "chain starts at %d has length %d" % (maxnum, maxchain)

if __name__ == '__main__':
    benchmark(problem, solve)
