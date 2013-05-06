#!/usr/bin/env python

import math

from problem import Problem


class P31_40(Problem):

    def p34(self):
        """Digit factorials"""
        # 9! = 362880, 7 digit maximum
        LIMIT = math.factorial(9) * 7
        dsum = 0
        fdiff = [math.factorial(x) - 1 for x in xrange(10)]
        for i in xrange(10, LIMIT + 1, 10):
            x = i
            s = 0
            while x > 0:
                s += math.factorial(x % 10)
                x /= 10
            for lastdigit in xrange(10):
                tempsum = s + fdiff[lastdigit]
                if tempsum == i + lastdigit:
                    dsum += tempsum
                    if lastdigit == 2:
                        break
                elif tempsum > i + lastdigit and lastdigit == 2:
                    break
        print dsum

if __name__ == '__main__':
    p = P31_40()
    p.solve_all()
