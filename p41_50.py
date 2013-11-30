#!/usr/bin/env python

import itertools

from p1_10 import P1_10
from problem import Problem


class P41_50(Problem):

    def p41(self):
        """Pandigital prime"""
        pandigital = []
        pan_str = '987654321'
        for idx in range(len(pan_str)):
            for i in itertools.permutations(pan_str[idx:]):
                pandigital.append(int(''.join(i)))
            p = P1_10()
            for i in pandigital:
                if p._is_prime(i):
                    print(i)
                    return
            del pandigital[:]

    def p42(self):
        """Coded triangle numbers"""
        trinum_count = lambda x: 0 if ((8 * x + 1) ** 0.5 - 1) % 2 else 1
        word_value = lambda s: sum([ord(c.upper()) - ord('A') + 1 for c in s])
        with open('data/p42_words.txt', 'r') as f:
            words = [s.strip('\".\"') for s in f.read().split(',')]
            print(sum([trinum_count(word_value(w)) for w in words]))

if __name__ == '__main__':
    p = P41_50()
    p.solve_all()
