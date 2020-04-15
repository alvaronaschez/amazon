"""
https://en.wikipedia.org/wiki/Continuous_knapsack_problem
https://rosettacode.org/wiki/Knapsack_problem/Continuous
https://rosettacode.org/wiki/Knapsack_problem
"""
from typing import List
from operator import truediv
import unittest


def continuous_knapsack(weights: List[float], values: List[float], max_weight: float) -> float:
    """
    greedy algorithm
    """
    result = 0
    for value, weight in sorted(zip(values, weights), key=lambda x: truediv(*x), reverse=True):
        if weight <= max_weight:
            result += value
            max_weight -= weight
        else:  # weight > max_weight:
            result += (value/weight)*max_weight
            max_weight = 0
            break
    return result


class TestContinuousKnapsack(unittest.TestCase):
    def test_continuous_knapsack(self):
        weights = [3.8, 5.4, 3.6, 2.4, 4.0, 2.5, 3.7, 3.0, 5.9]
        values = [36.0, 43.0, 90.0, 45.0, 30.0, 56.0, 67.0, 95.0, 98.0]
        max_weight = 15.0
        expected_result = 349.38
        result = continuous_knapsack(weights, values, max_weight)
        self.assertAlmostEqual(result, expected_result, places=2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
