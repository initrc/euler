#!/usr/bin/env python

import itertools

from p1_10 import P1_10
from problem import Problem


class P41_50(Problem):

    def p41(self):
        """Pandigital prime"""
        pandigital = []
        pan_str = '987654321'
        for idx in xrange(len(pan_str)):
            for i in itertools.permutations(pan_str[idx:]):
                pandigital.append(int(''.join(i)))
            p = P1_10()
            for i in pandigital:
                if p._is_prime(i):
                    print i
                    return
            del pandigital[:]

if __name__ == '__main__':
    p = P41_50()
    p.solve_largest()
