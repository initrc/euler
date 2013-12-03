#!/usr/bin/env python

from util.benchmark import benchmark

problem = "17. Number letter counts"
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""


def solve():
    """Number letter counts"""
    sum = 0
    for x in range(1, 1001):
        sum += lettercounts(x)
    return sum


def lettercounts(x):
    rules = {
        1: len("one"),
        2: len("two"),
        3: len("three"),
        4: len("four"),
        5: len("five"),
        6: len("six"),
        7: len("seven"),
        8: len("eight"),
        9: len("nine"),
        10: len("ten"),
        11: len("eleven"),
        12: len("twelve"),
        13: len("thirteen"),
        14: len("fourteen"),
        15: len("fifteen"),
        16: len("sixteen"),
        17: len("seventeen"),
        18: len("eighteen"),
        19: len("nineteen"),
        20: len("twenty"),
        30: len("thirty"),
        40: len("forty"),
        50: len("fifty"),
        60: len("sixty"),
        70: len("seventy"),
        80: len("eighty"),
        90: len("ninety"),
        100: len("hundred"),
        1000: len("thousand")}
    if x == 0:
        return 0
    if x <= 20:
        return rules[x]
    elif x <= 99:
        if x in rules:
            return rules[x]
        else:
            return rules[x % 10] + rules[x // 10 * 10]
    elif x <= 999:
        digit2 = len("and") + lettercounts(x % 100) if x % 100 else 0
        return rules[x // 100] + rules[100] + digit2
    elif x <= 20000:
        digit3 = len("and") + lettercounts(x % 1000) if x % 1000 else 0
        return rules[x // 1000] + rules[1000] + digit3
    else:
        return 0  # unsupported

if __name__ == '__main__':
    benchmark(problem, solve)
