#!/usr/bin/env python

from util.benchmark import benchmark

problem = "5. Smallest multiple"
"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def solve():
    """Smallest multiple"""
    primes = (2, 3, 5, 7, 11, 13, 17, 19)
    primeidx = 0
    count = 20
    lcm = 1
    nums = list(range(1, count + 1))
    countof1 = 1
    # [1, 2, ..., 20] => [1, 1, ..., 1] by dividing primes
    while countof1 < count:
        isfactor = False
        for idx, num in enumerate(nums):
            if not num % primes[primeidx]:
                nums[idx] = num // primes[primeidx]
                if nums[idx] == 1:
                    countof1 += 1
                isfactor = True
        if isfactor:
            lcm *= primes[primeidx]
        else:
            primeidx += 1
    return lcm

if __name__ == '__main__':
    benchmark(problem, solve)
