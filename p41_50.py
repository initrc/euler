#!/usr/bin/env python

import itertools
from sets import Set

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

    def p42(self):
        """Coded triangle numbers"""
        count = 0
        tri_nums = Set()
        for i in xrange(1, 100):
            tri_nums.add(i * (i+1) / 2)
        with open('data/p42_words.txt', 'r') as f:
            words = [s.strip('\".\"') for s in f.read().split(',')]
            for word in words:
                if sum([ord(c) - 64 for c in word]) in tri_nums:
                    count += 1
        print count

if __name__ == '__main__':
    p = P41_50()
    p.solve_largest()
