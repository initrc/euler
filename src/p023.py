#!/usr/bin/env python

from util.benchmark import benchmark
from util.number import sumproperdivisors
from util.prime import primeset

problem = "23. Non-abundant sums"
"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""


def solve():
    """Non-abundant sums"""
    LIMIT = 28123
    primes = sorted(primeset(LIMIT + 1))
    isabundant = lambda x: sumproperdivisors(x, primes) > x
    abundant = list(filter(isabundant, range(2, LIMIT + 1)))
    abundantsum = set()
    for i in range(len(abundant)):
        if abundant[i] * 2 > LIMIT:
            return sum([x for x in range(1, LIMIT + 1) if x not in
                       abundantsum])
        for j in range(i, len(abundant)):
            s = abundant[i] + abundant[j]
            if s <= LIMIT:
                abundantsum.add(s)
            else:
                break

if __name__ == '__main__':
    benchmark(problem, solve)
