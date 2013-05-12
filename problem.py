#!/usr/bin/env python

import inspect
import time


class Problem:

    def __init__(self):
        """create problems dict"""
        self.problems = dict((int(x[1:]), y) for x, y in inspect.getmembers(
            self, predicate=inspect.ismethod) if x[0] == 'p')

    def solve(self, id):
        """solve a problem and measure the time"""
        start = time.time()
        self.problems[id]()
        end = time.time()
        print "[problem %d: %fs]\n" % (id, end - start)

    def solve_largest(self):
        """solve the largest problem"""
        self.solve(max(self.problems.keys()))

    def solve_all(self):
        """solve all problems"""
        for id in sorted(self.problems.keys()):
            self.solve(id)
