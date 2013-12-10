#!/usr/bin/env python

import os
import p018
from util.benchmark import benchmark

problem = "67. Maximum path sum II"
"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt
(right click and 'Save Link/Target As...'), a 15K text file containing a
triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)
"""


def solve():
    """Maximum path sum II"""
    """Maximum path sum I at p18"""
    file = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir,
                           'data', 'p67_triangle.txt'))
    with open(file, 'r') as f:
        tree = [[p018.TreeNode(int(x)) for x in x.split()]
                for x in f.readlines()]
        return p018.solve(tree)


if __name__ == '__main__':
    benchmark(problem, solve)
