from functools import reduce
from math import gcd
import sys
import re
import random
import os
import math
# gdc subsequence


#!/bin/python3


#
# Complete the 'findSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#

"""
habia que hacer el maximo comun divisor (greatest common divisor) de un grupo de al menos k numeros
de entre una secuencia de numeros (con más de k números)
por ejemplo si numbers = [2,7,8,13, 29, 3, 256] y k=3
el maximo comun divisor es 2 y el grupo de numeros es [2, 8, 256]

había que devolver una lista con los integrantes de la secuencia,
pero en esta versión yo sólo devuelvo el gcd (as an int)
la version que entregue si devolvia la lista
"""


def multigcd(a):
    return reduce(gcd, a)


def findSubsequence(numbers, k):
    m = max(numbers)
    a = [False]*(m+1)
    for n in numbers:
        a[n] = True
    x = 1
    for n in numbers:
        z = 1
        for i in range(2, m//n):
            if a[i*n]:
                z += 1
        if z >= k and n > x:
            x = n
    return x


if __name__ == '__main__':
    pass
