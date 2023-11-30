#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    D = b * b - 4 * a * c

    if D < 0 and c > 0:
        print("(-inf;inf)")
    elif D < 0 and c < 0:
        print("Пустое множество")
    else:
        x_first = (-b - math.sqrt(D))/(2*a)
        x_second = (-b + math.sqrt(D)) / (2 * a)
        if x_first > x_second:
            x_first,x_second = x_second,x_first
        if a < 0:
            print(f"Ответ: ({x_first};{x_second})")
        else:
            print(f"Ответ: (-inf,{x_first}) and ({x_second};inf)")