#!/usr/bin/env python

from p11_20 import P11_20, TreeNode
from problem import Problem


class P61_70(Problem):

    def p67(self):
        """Maximum path sum II"""
        """Maximum path sum I at p18"""
        p = P11_20()
        p.p18(self._p67_build_tree())

    def _p67_build_tree(self):
        with open('data/p67_triangle.txt', 'r') as f:
            return [map(lambda x: TreeNode(int(x)), x.split())
                    for x in f.readlines()]


if __name__ == '__main__':
    p = P61_70()
    p.solve_all()
