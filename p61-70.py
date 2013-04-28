#!/usr/bin/env python

import math
from p11_20 import P11_20
from problem import Problem
from sets import Set


class P61_70(Problem):

    def p67(self):
        """Maximum path sum II"""
        """Maximum path sum I at p18"""
        p = P11_20()
        p.p18(self._p67_build_tree())

    def _p67_build_tree(self):
        with open('data/triangle.txt', 'r') as f:
            return [map(lambda x: TreeNode(int(x)), x.split())
                    for x in f.readlines()]


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.value_above = 0

    def visit(self):
        self.value += self.value_above

if __name__ == '__main__':
    p = P61_70()
    p.solve_all()
