#!/usr/bin/env python

import math
import operator
from functools import reduce


def numofdivisors(x):
    num = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if not x % i:
            num += 1
    return num * 2


def properdivisors(num, primes):
    if num < 2:
        return []
    primedivisors = []
    x = num
    for prime in primes:
        if x == 1:
            break
        primecount = 0
        while not x % prime:
            primecount += 1
            x //= prime
        if primecount > 0:
            primedivisors.append((prime, primecount))
    return primedivisors


def divisorgen(primedivisors):
    if not primedivisors:
        return
    length = len(primedivisors)
    power = [0] * length
    while True:
        yield reduce(operator.mul, [primedivisors[i][0] ** power[i]
                                    for i in range(length)])
        idx = 0
        while True:
            power[idx] += 1
            if power[idx] <= primedivisors[idx][1]:
                break
            power[idx] = 0
            idx += 1
            if idx >= length:
                return


def sumproperdivisors(num, primes):
    if num < 2:
        return 0
    primedivisors = properdivisors(num, primes)
    return sum([i for i in divisorgen(primedivisors)]) - num
