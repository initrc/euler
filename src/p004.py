#!/usr/bin/env python

import math
from util.benchmark import benchmark

problem = "4. Largest palindrome product"
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def solve():
    """Largest palindrome product"""
    max, x1, x2, xmax, xmin = -1, -1, -1, 999, 100
    # the largest is at least 6 digits, 111111 = 777 * 143
    # abccba = 100001*a + 10010*b + 1100*c, mutiple of 11

    for i in range(990, xmin, -11):
        for j in range(xmax, xmin, -1):
            p = i * j
            if p < max:
                if j == xmax:
                    return "%d = %d * %d" % (max, x1, x2)
                else:
                    break
            if is_palindrome(p):
                max, x1, x2 = p, i, j


def is_palindrome(x):
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
        reverse_x += num // base * multi
        num %= base
        base //= 10
        multi *= 10
    return x == reverse_x


if __name__ == '__main__':
    benchmark(problem, solve)
