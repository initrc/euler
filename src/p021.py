#!/usr/bin/env python

from util.benchmark import benchmark
from util.number import sumproperdivisors
from util.prime import primeset

problem = "21. Amicable numbers"
"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def solve():
    """Amicable numbers"""
    primes = sorted(primeset(10000))
    amicable = set()
    for x in range(1, 10000):
        if x in amicable:
            continue
        y = sumproperdivisors(x, primes)
        if x != y and x == sumproperdivisors(y, primes):
            amicable.add(x)
            if y < 10000:
                amicable.add(y)
    return sum(amicable)


if __name__ == '__main__':
    benchmark(problem, solve)
