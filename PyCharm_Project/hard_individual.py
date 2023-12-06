#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from decimal import *
import math
import sys


getcontext().prec = 4096
EULER = 0.5772156649015328606
EPS = 1e-10

if __name__ == '__main__':
    x = Decimal(input("Value of x? "))

    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    S = Decimal(0)
    a = Decimal(1)
    n = Decimal(1)

    while Decimal(math.fabs(a)) > EPS:
        e0 = Decimal((-1)**n)
        e1 = Decimal(x**(2*n))
        e2 = Decimal(2*n)
        e3 = Decimal(1)
        temp = 2*n
        while temp > 1:
             e3 *= temp
             temp -= 1
        a = (e0*e1)/(e2*e3)
        n += 1
        S += a

    print(f"\nCi({x}) = {EULER + math.log(x) + float(S)}")
