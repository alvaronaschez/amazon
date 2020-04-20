"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2963/

Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

import unittest
from typing import List


def max_area(a: List[int]) -> int:
    result = 0
    i = 0
    j = len(a) - 1
    while i < j:
        x = (j-i)*min(a[i], a[j])
        result = max(result, x)
        if a[i] >= a[j]:
            j -= 1
        else:
            i += 1
    return result


def max_area_naive(a: List[int]) -> int:
    # naive approach
    result = 0
    for i, n in enumerate(a):
        for j, m in enumerate(a[i+1:], i+1):
            x = (j-i)*min(n, m)
            result = max(result, x)
    return result


class TestMaxArea(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)


if __name__ == "__main__":
    unittest.main(verbosity=2)
