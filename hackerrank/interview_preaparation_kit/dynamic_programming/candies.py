"""
https://www.hackerrank.com/challenges/candies/
"""


def candies(n, arr):
    result = [1]*n
    for (i, prev), (j, curr) in zip(enumerate(arr, 0), enumerate(arr[1:], 1)):
        if prev < curr:
            result[j] = result[i]+1
    for (i, prev), (j, curr) in zip(enumerate(arr[::-1], 1), enumerate(arr[::-1][1:], 2)):
        if prev < curr:
            result[-j] = max(result[-i]+1, result[-j])
    return sum(result)
