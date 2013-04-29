#!/usr/bin/env python

import math
from problem import Problem
from sets import Set


class P1_10(Problem):

    def p1(self):
        """Multiples of 3 and 5"""
        sum = 0
        for i in range(1, 1000):
            if not i % 3 or not i % 5:
                sum += i
        print sum

    def p2(self):
        """Even Fibonacci numbers"""
        sum, a, b = 0, 1, 2
        while b < 4000000:
            sum += b
            # a(odd), b(even), a+b(odd), a+2b(odd), 2a+3b(even)
            a, b = a + 2 * b, 2 * a + 3 * b
        print sum

    def p3(self):
        """Largest prime factor"""
        x = 600851475143
        factor, max_factor = 2, 2
        # x has at most one factor that is greater than sqrt(x)
        gate = math.sqrt(x)
        while factor <= gate:
            if not x % factor:
                x /= factor
                max_factor = factor
            else:
                factor += 1
        print max_factor if x == 1 else x

    def p4(self):
        """Largest palindrome product"""
        a, max, x1, x2 = 999, -1, -1, -1
        # if 6 digit, must be a multiple of 11
        # 111111 = 777 * 143
        for i in range(990, 109, -11):
        # or brute force
        # for i in range(a, 0, -1):
            for j in range(a, 0, -1):
                p = i * j
                if p < max:
                    if j == a:
                        print "%d = %d * %d" % (max, x1, x2)
                        return
                    else:
                        break
                if self._p4_is_palindrome(p):
                    max, x1, x2 = p, i, j

    def _p4_is_palindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        digit = int(math.log(x, 10)) + 1
        base = 10 ** (digit - 1)
        reverse_x = 0
        multi = 1
        num = x
        for i in range(digit):
            reverse_x += num / base * multi
            num %= base
            base /= 10
            multi *= 10
        return x == reverse_x

    def p5(self):
        """Smallest multiple"""
        primes = (2, 3, 5, 7, 11, 13, 17, 19)
        prime_idx = 0
        count = 20
        lcm = 1
        nums = range(1, count + 1)
        count_of_1 = 1
        while count_of_1 < count:
            is_divider = False
            for idx, num in enumerate(nums):
                if not num % primes[prime_idx]:
                    nums[idx] = num / primes[prime_idx]
                    if nums[idx] == 1:
                        count_of_1 += 1
                    is_divider = True
            if is_divider:
                lcm *= primes[prime_idx]
            else:
                prime_idx += 1
        print lcm

    def p6(self):
        """Sum square difference"""
        count = 100
        nums = range(1, count + 1)
        sum_of_squares = 0
        for i in nums:
            sum_of_squares += i ** 2
        square_of_sum = sum(nums) ** 2
        print square_of_sum - sum_of_squares
        # or get the formula f(n) = 1^2 + ... + n^2

    def p7(self):
        """10001st prime"""
        x = 3
        idx = 3
        while idx <= 10001:
            x += 2
            if self._p7_is_prime(x):
                idx += 1
        print x

    def _p7_is_prime(self, x):
        if not x % 2:
            return False
        factor = 3
        gate = int(math.sqrt(x))
        while factor <= gate:
            if not x % factor:
                return False
            else:
                factor += 2
        return True
        # prime > 3 can be represented in the form of 6k+-1

    def p8(self):
        """Largest product in a series"""
        num = ("73167176531330624919225119674426574742355349194934"
               "96983520312774506326239578318016984801869478851843"
               "85861560789112949495459501737958331952853208805511"
               "12540698747158523863050715693290963295227443043557"
               "66896648950445244523161731856403098711121722383113"
               "62229893423380308135336276614282806444486645238749"
               "30358907296290491560440772390713810515859307960866"
               "70172427121883998797908792274921901699720888093776"
               "65727333001053367881220235421809751254540594752243"
               "52584907711670556013604839586446706324415722155397"
               "53697817977846174064955149290862569321978468622482"
               "83972241375657056057490261407972968652414535100474"
               "82166370484403199890008895243450658541227588666881"
               "16427171479924442928230863465674813919123162824586"
               "17866458359124566529476545682848912883142607690042"
               "24219022671055626321111109370544217506941658960408"
               "07198403850962455444362981230987879927244284909188"
               "84580156166097919133875499200524063689912560717606"
               "05886116467109405077541002256983155200055935729725"
               "71636269561882670428252483600823257530420752963450")
        product = self._p8_product_of_str(num[:5])
        cur_idx = 0
        next_idx = 5
        while next_idx < len(num):
            jump = False
            while True:
                zero_idx = self._p8_has_0(num[cur_idx:next_idx])
                if zero_idx != -1:
                    cur_idx += zero_idx + 1
                    next_idx += zero_idx + 1
                    jump = True
                else:
                    break
            if jump or int(num[next_idx]) > int(num[cur_idx]):
                product = max(product, self._p8_product_of_str(
                    num[cur_idx + 1:next_idx + 1]))
            cur_idx += 1
            next_idx += 1
        print product

    def _p8_product_of_str(self, str):
        product = 1
        for i in str:
            product *= int(i)
        return product

    def _p8_has_0(self, str):
        idx = -1
        for i in range(len(str)):
            if (int(str[i]) == 0):
                idx = i
        return idx

    def p9(self):
        """Special Pythagorean triplet"""
        sum = 1000
        square_set = Set()
        for i in range(1, sum - 2):
            square_set.add(i * i)
        for a in range(1, sum / 3):
            for b in range(a + 1, sum / 2):
                c2 = a*a + b*b
                if c2 in square_set:
                    c = int(math.sqrt(c2))
                    if a + b + c == 1000:
                        print a, b, c, a*b*c
                        return

    def p10(self):
        """Summation of primes"""
        print sum(self._p10_prime_set(2000000))

    def _p10_prime_set(self, limit):
        set = Set([2, 3])
        for i in range(6, limit, 6):
            set.add(i - 1)
            set.add(i + 1)
        for i in range(5, int(math.sqrt(limit)) + 1, 2):
            for j in range(i * 3, limit, i):
                if j in set:
                    set.remove(j)
        return set


if __name__ == '__main__':
    p = P1_10()
    p.solve_all()
