#!/usr/bin/env python

import subprocess
import sys


def benchmark(problems):
    for x in problems:
        subprocess.call(["python", "src/p%03d.py" % x])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(("\nUsage:\n"
               "./euler.sh [x]   : solves problem #x\n"
               "./euler.sh [x-y] : solves problems #x to #y\n"))
        exit(1)
    p = [int(x) for x in sys.argv[1].split("-")]
    if len(p) > 1:
        p = range(p[0], p[1] + 1)
    benchmark(p)
