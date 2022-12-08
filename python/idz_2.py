#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    l = list(map(int, input().split()))

    negative_list = list(filter(lambda x: x < 0, l))
    abs_list = [abs(i) for i in l]
    min_elem = min([i[1] for i in enumerate(abs_list)])
    summa = sum(abs_list[abs_list.index(min_elem):])

    print(f"There are {len(negative_list)} negative items in list")
    print(f"Summa is {summa}")
