#!/usr/bin/env python

import math
from sets import Set

from p1_10 import P1_10
from problem import Problem


class P31_40(Problem):

    def p34(self):
        """Digit factorials"""
        # 9! = 362880, 7 digit maximum
        LIMIT = math.factorial(9) * 7
        dsum = 0
        fdiff = [math.factorial(x) - 1 for x in xrange(10)]
        for i in xrange(10, LIMIT + 1, 10):
            x = i
            s = 0
            while x > 0:
                s += math.factorial(x % 10)
                x /= 10
            for lastdigit in xrange(10):
                tempsum = s + fdiff[lastdigit]
                if tempsum == i + lastdigit:
                    dsum += tempsum
                    if lastdigit == 2:
                        break
                elif tempsum > i + lastdigit and lastdigit == 2:
                    break
        print dsum

    def p35(self):
        """Circular primes"""
        LIMIT = 1000000
        primes = P1_10()._prime_set(LIMIT)
        circular_primes = Set()
        digitnum = lambda x: int(math.log10(x) + 1)
        rotate = lambda x, d: x % 10 * 10**d + x / 10
        for x in primes:
            if x in circular_primes:
                continue
            circular = True
            nrotate = digitnum(x) - 1
            for d in xrange(nrotate):
                x = rotate(x, nrotate)
                if x not in primes:
                    circular = False
                    break
            if circular:
                for d in xrange(nrotate + 1):
                    circular_primes.add(x)
                    x = rotate(x, nrotate)
        print len(circular_primes)

if __name__ == '__main__':
    p = P31_40()
    p.solve_largest()
