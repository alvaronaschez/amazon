"""
https://rosettacode.org/wiki/Knapsack_problem/0-1
https://rosettacode.org/wiki/Knapsack_problem
"""
import unittest
from math import inf


def knapsack_01(weights, values, max_weight):
    """
    dynamic programming algorithm
    based on the following recursive definition:

    knapsack(i, w) = -inf if w<0
    knapsack(i, w) = 0 if i=-1 or w=0
    knapsack(i, w) = max( v[i] + knapsack(i-1, w-w[i]), knapsack(i-1, w) otherwise

    where i is the last explored item
    and w the remaining capacity of the knapsack
    """
    n = len(weights)
    aux = [[0]*(max_weight+1) for _ in range(n)]

    def read(i, w):
        if w < 0:
            return -inf
        elif i == -1 or w == 0:
            return 0
        else:
            return aux[i][w]

    for i in range(n):
        for j in range(max_weight+1):
            aux[i][j] = max(
                read(i-1, j-weights[i]) + values[i],
                read(i-1, j)
            )
    return read(n-1, max_weight)


class TestKnapsack01(unittest.TestCase):
    def test_knapsack_01(self):
        weights = [9, 13, 153, 50, 15, 68, 27, 39, 23, 52,
                   11, 32, 24, 48, 73, 42, 43, 22, 7, 18, 4, 30]
        values = [150, 35, 200, 160, 60, 45, 60, 40, 30, 10,
                  70, 30, 15, 10, 40, 70, 75, 80, 20, 12, 50, 10]
        max_weight = 400
        expected_result = 1030
        result = knapsack_01(weights, values, max_weight)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
