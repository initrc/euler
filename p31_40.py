#!/usr/bin/env python

import itertools
import math

from p1_10 import P1_10
from problem import Problem


class P31_40(Problem):

    def p31(self):
        """Coin sums"""
        """Bottom-up dynamic programming - Project Euler answer"""
        """
        w(t, c) = 1                      if c = 1 or t = 0
        w(t, c) = w(t, s(c))             if c > 1 and t < c
        w(t, c) = w(t, s(c)) + w(t-c, c) if c > 1 and t >= c
        t = target amount
        c = the value of the largest available coin
        s(c) = the value of the next coin small than c
        w(t, c) = the number of ways to make the target amount t
        with coins of value c and/or small coins
        """
        coins = [1, 2, 5, 10, 20, 50, 100, 200]
        amount = 200
        ways = [0] * (amount + 1)
        ways[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                ways[i] += ways[i - coin]
        print(ways[amount])

    def _p31_with_product(self):
        """Coin sums"""
        """Solve with dynamic product"""
        sol_count = 0
        coins = [100, 50, 20, 10, 5]
        max_picks = [200 // i for i in coins]
        n = len(coins)
        picks = [0] * n
        coinsum = lambda: sum(c * p for c, p in zip(coins, picks))
        for picks in self._dynamic_product(max_picks):
            s = coinsum()
            if s > 200:
                continue
            sol_count += (200-s)//2 + 1
        print(sol_count + 1)

    def _dynamic_product(self, itercounts):
        """A simple dynamic version of itertools.product"""
        """itercounts is a list of iteration numbers"""
        result = [[]]
        for pool in [range(x + 1) for x in itercounts]:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield prod

    def p32(self):
        """Pandigital products"""
        pandigital = set()
        digit_num = lambda x: int(math.log10(x) + 1)
        list_mul = lambda x, y: [i * j for i, j in zip(x, y)]

        for a in range(2, 100):
            a_digits = self._digits(a)
            if a_digits is None:
                continue
            a_digit_num = digit_num(a)
            b_digit_num = 5 - a_digit_num
            b_start = pow(10, b_digit_num - 1)
            for b in range(b_start, b_start * 10):
                c = a * b
                c_digit_num = digit_num(c)
                if c_digit_num > 4:
                    break
                b_digits = self._digits(b)
                if b_digits is None or sum(list_mul(a_digits, b_digits)):
                    continue
                c_digits = self._digits(c)
                if c_digits is None:
                    continue
                is_pandigital = True
                for i in range(9):
                    if (a_digits[i] + b_digits[i] + c_digits[i]) != 1:
                        is_pandigital = False
                        break
                if is_pandigital:
                    pandigital.add(c)
                    print("%d * %d = %d" % (a, b, c))
        print(sum(pandigital))

    def _digits(self, num):
        """Return a list of digits or None if there are duplicates"""
        digits = [0] * 9
        while num > 0:
            digit = num % 10
            if digit == 0 or digits[digit - 1] == 1:
                return None
            digits[digit - 1] = 1
            num //= 10
        return digits

    def p33(self):
        """Digit canceling fractions"""
        """ab//bc = a//c"""
        numerator, denominator, factor = 1, 1, 2
        for b in range(1, 10):
            for a, c in itertools.product(list(range(1, 10)), repeat=2):
                if a == b or c == b:
                    continue
                if (a*10+b) * c == (b*10+c) * a:
                    print("%d/%d = %d/%d" % (a*10+b, b*10+c, a, c))
                    numerator *= a
                    denominator *= c
        while factor <= numerator:
            if not numerator % factor and not denominator % factor:
                numerator //= factor
                denominator //= factor
            else:
                factor += 1
        print(denominator)

    def p34(self):
        """Digit factorials"""
        # 9! = 362880, 7 digit maximum
        LIMIT = math.factorial(9) * 7
        dsum = 0
        fdiff = [math.factorial(x) - 1 for x in range(10)]
        for i in range(10, LIMIT + 1, 10):
            x = i
            s = 0
            while x > 0:
                s += math.factorial(x % 10)
                x //= 10
            for lastdigit in range(10):
                tempsum = s + fdiff[lastdigit]
                if tempsum == i + lastdigit:
                    dsum += tempsum
                    if lastdigit == 2:
                        break
                elif tempsum > i + lastdigit and lastdigit == 2:
                    break
        print(dsum)

    def p35(self):
        """Circular primes"""
        LIMIT = 1000000
        primes = P1_10()._prime_set(LIMIT)
        circular_primes = set()
        digitnum = lambda x: int(math.log10(x) + 1)
        rotate = lambda x, d: x % 10 * 10**d + x // 10
        for x in primes:
            if x in circular_primes:
                continue
            circular = True
            nrotate = digitnum(x) - 1
            for d in range(nrotate):
                x = rotate(x, nrotate)
                if x not in primes:
                    circular = False
                    break
            if circular:
                for d in range(nrotate + 1):
                    circular_primes.add(x)
                    x = rotate(x, nrotate)
        print(len(circular_primes))

    def p36(self):
        """Double-base palindromes"""
        LIMIT = 1000000
        print(sum([x for x in range(1, LIMIT) if str(x) == str(x)[::-1]
                   and bin(x)[2:] == bin(x)[:1:-1]]))

    def p37(self):
        """Truncatable primes"""
        LIMIT = 1000000
        count = 0
        prime_sum = 0
        primes = P1_10()._prime_set(LIMIT)
        primes_list = sorted(primes)
        for prime in primes_list[4:]:
            truncatable = True
            for d in [pow(10, i + 1) for i in range(int(math.log10(prime)))]:
                if prime // d not in primes or prime % d not in primes:
                    truncatable = False
                    break
            if truncatable:
                prime_sum += prime
                count += 1
            if count == 11:
                break
        print(prime_sum)

    def p38(self):
        """Pandigital multiples"""
        """
        The multiplicand starts with 9
        9: 918273645
        9x: 2+3+3 = 8 digits
        9xx: 3+4+4 = 11 digits
        9xxx: 4+5 = 9 digits, possible answer that is > 918273645
        """
        max_pandigital = 918273645
        # if a >= 9500, b = 19xxx that contains 9
        for a in range(9182, 9500):
            a_digits = self._digits(a)
            if a_digits is None:
                continue
            b = a * 2
            b_digits = self._digits(b)
            if b_digits is None:
                continue
            is_pandigital = True
            for i in range(9):
                if a_digits[i] + b_digits[i] != 1:
                    is_pandigital = False
                    break
            if is_pandigital:
                pandigital = a * 100002
                max_pandigital = max(pandigital, max_pandigital)
        print(max_pandigital)

    def p39(self):
        """Integer right triangles"""
        finalp = 120
        sol_num = 3
        LIMIT = 1000
        square_diff = lambda a, b, p: a**2 + b**2 - (p-a-b)**2
        for p in range(5, LIMIT + 1):
            cur_sol_num = 0
            for a in range(1, p // 3):
                bstart = max(a, p//2 - a)
                for b in range(bstart, (p-a)//2 - 1):
                    diff = square_diff(a, b, p)
                    if diff == 0:
                        cur_sol_num += 1
                    elif diff > 0:
                        break
            if cur_sol_num > sol_num:
                sol_num = cur_sol_num
                finalp = p
        print("p=%d, max number of solution=%d" % (finalp, sol_num))

    def p40(self):
        """Champernowne's constant"""
        pos = {1: 1}
        i, finalp, LIMIT = 1, 1, 6
        while pos[i] < 10 ** LIMIT:
            j = i * 10
            pos[j] = pos[i] + (j-i) * int(math.log10(j))
            i = j
        for x in [10 ** k for k in range(LIMIT + 1)]:
            for y in sorted(pos.keys()):
                if pos[y] == x:
                    # finalp *= 1
                    break
                elif pos[y] > x:
                    y = y // 10
                    diff = x - pos[y]
                    digit = int(math.log10(y) + 1)
                    num = diff // digit + y
                    bit = diff % digit
                    finalp *= int(str(num)[bit])
                    break
        print(finalp)

if __name__ == '__main__':
    p = P31_40()
    p.solve_all()
