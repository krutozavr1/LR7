#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    l = list(map(int, input().split()))

    sorted_list = list(filter(lambda x: 8 < x < 18, l))
    cnt = 0
    result = 1

    for i in sorted_list:
        if i % 10 == 0:
            cnt += 1
            result *= i

    print(f"Result is {result}, cnt is {cnt}")
