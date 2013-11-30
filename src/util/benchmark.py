#!/usr/bin/env python
from time import time


def benchmark(name, solve):
    """judge the solution"""
    start = time()
    solution = solve()
    end = time()
    print("%s\n%s\n[%fs]\n" % (name, solution, end - start))
