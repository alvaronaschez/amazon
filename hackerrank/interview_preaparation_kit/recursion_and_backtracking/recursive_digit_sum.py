"""
https://www.hackerrank.com/challenges/recursive-digit-sum/
"""
from functools import wraps
from collections import Counter
from random import randrange
import time
from math import log, ceil


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(func.__name__, ':', elapsed)
    return wrapper


def superDigit_v1(n, k):
    """too slow: didn't pass two test cases due to timeout"""
    def gen(n: int):
        while n > 0:
            yield n % 10
            n //= 10
    n = int(n)
    n = sum(gen(n))
    while n > 9:
        n = sum(gen(n))
    while k > 9:
        k = sum(gen(k))
    n *= k
    while n > 9:
        n = sum(gen(n))
    return n


@timer
def superDigit_v2(n: str, k: int) -> int:
    """
    digit Counter version
    slowler than the divide and conquer version v3
    """
    while len(n) > 1:
        c = Counter(n)
        n = sum(int(k)*v for k, v in c.items())
        n = str(n)
    n = int(n)
    if k == 1:
        return n
    else:
        return superDigit_v2(str(n*k), 1)


@timer
def superDigit_v3(n: str, k: int) -> int:
    """
    divide and conquer recursive version
    the second fastest after v5
    """
    def super_digit(n: str) -> int:
        if len(n) == 1:
            return int(n)
        else:
            i = len(n)//2
            x = super_digit(n[:i])
            y = super_digit(n[i:])
            return super_digit(str(x+y))
    n = super_digit(n)
    return super_digit(str(n*k))


@timer
def superDigit_v4(n: str, k: int) -> int:
    """
    v2 refactored version
    slowler than the divide and conquer version v3
    """
    def super_digit(n):
        while len(n) > 1:
            c = Counter(n)
            n = sum(int(k)*v for k, v in c.items())
            n = str(n)
        return int(n)
    return super_digit(str(k*super_digit(n)))


@timer
def superDigit_v5(n: str, k: int) -> int:
    """
    v3 turned into iterative
    now this is the fastest version
    """
    def super_digit(n: int) -> int:
        while n > 9:
            l = log(n, 10)
            m = int(10**ceil(l/2))
            x = n//m
            y = n % m
            n = x+y
        return n
    n = int(n)
    return super_digit(k*super_digit(n))


x = randrange(10**20, 10**21)
y = randrange(10**20, 10**21)
x = str(x)

t = superDigit_v3(x, y)
z = superDigit_v5(x, y)

assert z == t
