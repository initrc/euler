#!/usr/bin/env python

import itertools
import operator

from p1_10 import P1_10
from problem import Problem
from functools import reduce


class P21_30(Problem):

    def p21(self):
        """Amicable numbers"""
        primes = sorted(P1_10()._prime_set(10000))
        amicable = set()
        for x in range(1, 10000):
            if x in amicable:
                continue
            y = self._proper_divisor_sum(x, primes)
            if x != y and x == self._proper_divisor_sum(y, primes):
                amicable.add(x)
                if y < 10000:
                    amicable.add(y)
        print(sum(amicable))

    def _proper_divisor_sum(self, num, primes):
        if num < 2:
            return 0
        prime_divisors = []
        x = num
        for prime in primes:
            if x == 1:
                break
            prime_count = 0
            while not x % prime:
                prime_count += 1
                x //= prime
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
                                        for i in range(length)])
            idx = 0
            while True:
                power[idx] += 1
                if power[idx] <= prime_divisors[idx][1]:
                    break
                power[idx] = 0
                idx += 1
                if idx >= length:
                    return

    def p22(self):
        """Names scores"""
        with open('data/p22_names.txt', 'r') as f:
            names = [s.strip('\".\"') for s in f.read().split(',')]
        score = 0
        for idx, name in enumerate(sorted(names)):
            s = sum(ord(c) - 64 for c in name)
            score += s * (idx + 1)
        print(score)

    def p23(self):
        """Non-abundant sums"""
        LIMIT = 28123
        primes = sorted(P1_10()._prime_set(LIMIT + 1))
        is_abundant = lambda x: self._proper_divisor_sum(x, primes) > x
        abundant = list(filter(is_abundant, range(2, LIMIT + 1)))
        abundant_sum = set()
        for i in range(len(abundant)):
            if abundant[i] * 2 > LIMIT:
                print(sum([x for x in range(1, LIMIT + 1) if x not in
                           abundant_sum]))
                return
            for j in range(i, len(abundant)):
                s = abundant[i] + abundant[j]
                if s <= LIMIT:
                    abundant_sum.add(s)
                else:
                    break

    def p24(self):
        """Lexicographic permutations"""
        LIMIT = 1000000
        p = itertools.permutations(range(10))
        for i in range(LIMIT - 1):
            next(p)
        print(reduce(lambda x, y: x * 10 + y, next(p)))

    def p25(self):
        """1000-digit Fibonacci number"""
        i, j, idx = 1, 1, 2
        while j < 10 ** 999:
            i, j = j, i + j
            idx += 1
        print(idx)

    def p26(self):
        """Reciprocal cycles"""
        longest, d = 0, 0
        for x in range(2, 1000):
            idx, length = 0, 0
            remainders = {}
            dividend = 10
            while dividend < x:
                dividend *= 10
            remainder = dividend % x
            while remainder != 0:
                if remainder in remainders:
                    length = idx - remainders.get(remainder)
                    if length > longest:
                        longest = length
                        d = x
                    break
                remainders[remainder] = idx
                dividend = remainder * 10
                while dividend < x:
                    dividend *= 10
                    idx += 1
                remainder = dividend % x
                idx += 1
        print(d)

    def p27(self):
        """Quadratic primes"""
        # example: n^2 + n + 41 (n = 0 to 39)
        final_a, final_b = 1, 41
        max_n = 39
        LIMIT = 1000
        MAX_PRIME = 1601
        # a must be odd and b must be a prime
        f = lambda a, b, n: n ** 2 + a * n + b
        primes = P1_10()._prime_set(MAX_PRIME + 1)
        for b in [x for x in primes if x > 41 and x < 1000]:
            for a in range(1 - LIMIT, 1000, 2):
                if f(a, b, 40) in primes:
                    n = 0
                    while True:
                        if f(a, b, n) in primes:
                            n += 1
                        else:
                            if n > max_n:
                                max_n = n
                                final_a, final_b = a, b
                            break
        print("a=%d, b=%d, a*b=%d, n = 0 to %d" % (final_a, final_b,
                                                   final_a * final_b, max_n))

    def p28(self):
        """Number spiral diagonals"""
        """
        sum = 1 + 4 * (6 + 19 + ...)
        upper right = 3^2, 5^2, ...
        f(n) = n^2 - (n-1) - (n-1)//2 = n^2 - (n-1)*3//2
        f(3) = 6, f(5) = 19, ...
        """
        LIMIT = 1001
        f = lambda n: n ** 2 - (n - 1) * 3 // 2
        s = sum(map(f, range(3, LIMIT + 1, 2)))
        print(1 + s * 4)

    def p29(self):
        """Distinct powers"""
        s = set()
        for a in range(2, 101):
            for b in range(2, 101):
                s.add(a ** b)
        print(len(s))

    def p30(self):
        """Digit fifth powers"""
        sum = 0
        # 9^5=59049, at most 6 digits
        for i in range(2, 9**5 * 6 + 1):
            num = 0
            x = i
            while x > 0:
                num += (x % 10) ** 5
                x //= 10
            if num == i:
                sum += num
        print(sum)

if __name__ == '__main__':
    p = P21_30()
    p.solve_all()
