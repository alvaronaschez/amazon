#!/bin/python3

import math
import os
import random
import re
import sys


# user friendly password system
#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

"""
5
2
setPassword 1
setPassword 2
setPassword 3
authorize 49
authorize 50

my 1 1
correct 0 0

"""
P = 131
M = 10**9+7


def h(s):
    x = 0
    for i, c in enumerate(reversed(s)):
        x += ord(c)*P**i
    x = x % M
    return x


def set_password(w, s):
    x = 0
    for i, c in enumerate(reversed(w)):
        x += ord(c)*P**i
    s.add(x % M)
    for i in range(128):
        print((P*x+i) % M)
        s.add((P*x+i) % M)
    """
    for i in range(61,123):
        s.add((P*x+i)%M)
    for i in range(65,91):
        s.add((P*x+i)%M)
    for i in range(30,40):
        s.add((P*x+i)%M)
    """


def authEvents(events):
    s = set()
    result = []
    for e, w in events:
        if e == "setPassword":
            set_password(w, s)
        else:
            result.append(1 if int(w) in s else 0)
    return result


if __name__ == '__main__':
    pass
