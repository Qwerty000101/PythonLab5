#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    i = 10
    while i <= 100:
        if i%(int(str(i)[0])+int(str(i)[1])) == 0:
            result = int(i / (int(str(i)[0]) + int(str(i)[1])))
            print(f"{i}: {int(str(i)[0])} + {int(str(i)[1])} = {result}")
        i += 1