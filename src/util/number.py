#!/usr/bin/env python

import math


def numofdivisors(x):
    num = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if not x % i:
            num += 1
    return num * 2
