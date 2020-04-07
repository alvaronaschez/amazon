#!/bin/python3
"""
Making Candies
Haker Rank
https://www.hackerrank.com/challenges/making-candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
"""

import sys
from math import floor, ceil, inf


def minimumPasses(m, w, p, n):
    if p > n:
        return ceil(n/(m*w))

    m, w = sorted([m, w])
    c = 0
    i = 0
    j = inf
    while True:
        if c < p:
            x = ceil((p-c)/(m*w))
        else:
            x = 1
        i += x
        c += x*m*w

        if c > n:
            break

        j = min(j, i + ceil((n-c)/(m*w)))

        y = c//p
        c = c % p
        d = w-m
        m += min(d, y)
        y -= min(d, y)
        m += y//2
        w += y//2 + y % 2

    return min(i, j)
