#!/usr/bin/env python

import os
from util.benchmark import benchmark

problem = "22. Names scores"
"""
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def solve():
    """Names scores"""
    file = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir,
                           'data', 'p22_names.txt'))
    with open(file, 'r') as f:
        names = [s.strip('\".\"') for s in f.read().split(',')]
    score = 0
    for idx, name in enumerate(sorted(names)):
        s = sum(ord(c) - 64 for c in name)
        score += s * (idx + 1)
    return score

if __name__ == '__main__':
    benchmark(problem, solve)
