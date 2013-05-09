#!/usr/bin/env python

import itertools
import math
from sets import Set

from p1_10 import P1_10
from problem import Problem


class P31_40(Problem):

    def p31(self):
        """Coin sums"""
        sol_count = 0
        coins = [100, 50, 20, 10, 5]
        max_picks = [200 / i for i in coins]
        picks = [0] * len(coins)
        for picks in itertools.product(xrange(max_picks[-1] + 1),
                                       repeat=len(coins)):
            s = 0
            for coin, pick in zip(coins, picks):
                s += coin * pick
            if s > 200:
                continue
            exceed = False
            for max_pick, pick in zip(max_picks, picks):
                if max_pick < pick:
                    exceed = True
                    break
            if exceed:
                continue
            sol_count += (200-s)/2 + 1
            if picks[0] == 2:
                break
        print sol_count + 1

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

    def p36(self):
        """Double-base palindromes"""
        LIMIT = 1000000
        print sum([x for x in xrange(1, LIMIT) if str(x) == str(x)[::-1]
                   and bin(x)[2:] == bin(x)[:1:-1]])

    def p39(self):
        """Integer right triangles"""
        finalp = 120
        sol_num = 3
        LIMIT = 1000
        square_diff = lambda a, b, p: a**2 + b**2 - (p-a-b)**2
        for p in xrange(5, LIMIT + 1):
            cur_sol_num = 0
            for a in xrange(1, p / 3):
                bstart = max(a, int(p/2 - a))
                for b in xrange(bstart, int((p-a)/2 - 1)):
                    diff = square_diff(a, b, p)
                    if diff == 0:
                        cur_sol_num += 1
                    elif diff > 0:
                        break
            if cur_sol_num > sol_num:
                sol_num = cur_sol_num
                finalp = p
        print "p=%d, max number of solution=%d" % (finalp, sol_num)

    def p40(self):
        """Champernowne's constant"""
        pos = {1: 1}
        i, finalp, LIMIT = 1, 1, 6
        while pos[i] < 10 ** LIMIT:
            j = i * 10
            pos[j] = pos[i] + (j-i) * int(math.log10(j))
            i = j
        for x in [10 ** i for i in xrange(LIMIT + 1)]:
            for y in sorted(pos.keys()):
                if pos[y] == x:
                    # finalp *= 1
                    break
                elif pos[y] > x:
                    y = y / 10
                    diff = x - pos[y]
                    digit = int(math.log10(y) + 1)
                    num = diff / digit + y
                    bit = diff % digit
                    finalp *= int(str(num)[bit])
                    break
        print finalp

if __name__ == '__main__':
    p = P31_40()
    p.solve(31)
