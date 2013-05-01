#!/usr/bin/env python

import math
import operator
from sets import Set

from p1_10 import P1_10
from problem import Problem


class P21_30(Problem):

    def p21(self):
        """Amicable numbers"""
        primes = sorted(P1_10()._prime_set(10000))
        amicable = Set()
        for x in xrange(1, 10000):
            if x in amicable:
                continue
            y = self._proper_divisor_sum(x, primes)
            if x != y and x == self._proper_divisor_sum(y, primes):
                amicable.add(x)
                if y < 10000:
                    amicable.add(y)
        print sum(amicable)

    def _proper_divisor_sum(self, num, primes):
        if num < 2:
            return
        prime_divisors = []
        x = num
        for prime in primes:
            if x == 1:
                break
            prime_count = 0
            while not x % prime:
                prime_count += 1
                x /= prime
            if prime_count > 0:
                prime_divisors.append((prime, prime_count))
        if not prime_divisors:
            return 0
        return sum([i for i in self._divisor_gen(prime_divisors)]) - num

    def _divisor_gen(self, prime_divisors):
        length = len(prime_divisors)
        power = [0] * length
        while True:
            yield reduce(operator.mul, [prime_divisors[i][0] ** power[i]
                                        for i in xrange(length)])
            idx = 0
            while True:
                power[idx] += 1
                if power[idx] <= prime_divisors[idx][1]:
                    break
                power[idx] = 0
                idx += 1
                if idx >= length:
                    return

if __name__ == '__main__':
    p = P21_30()
    p.solve_largest()
