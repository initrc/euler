#!/usr/bin/env python

import math


def isprime(x):
    """Return True if x is prime, otherwise False"""
    if x < 2 or not x % 2:
        return False
    if x in (2, 3):
        return True
    # prime > 3 can be represented in the form of 6k+-1
    if x % 6 != 1 and x % 6 != 5:
        return False
    factor = 3
    gate = int(math.sqrt(x))
    while factor <= gate:
        if not x % factor:
            return False
        else:
            factor += 2
    return True


def primeset(limit):
    """Return primes below the limit"""
    # Sieve of Eratosthenes
    s = {2, 3}
    for i in range(6, limit, 6):
        s.add(i - 1)
        s.add(i + 1)
    # cross out multiple of primes
    for i in range(5, int(math.sqrt(limit)) + 1, 2):
        for j in range(i * 3, limit, i * 2):
            if j in s:
                s.remove(j)
    return s
