#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

if __name__ == '__main__':
    l = list(map(int, input().split()))

    sorted_list = list(filter(lambda x: 8 < x < 18, l))
    res_list = [i for i in sorted_list if i % 10 == 0]

    print(f"Result is {math.prod(res_list)}, cnt is {len(res_list)}")
