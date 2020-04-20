"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2975/


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

import unittest
from typing import List


def trap(h: List[int]) -> int:
    i = 0
    j = len(h)-1
    res = 0
    m = 0
    while i <= j:
        if h[i] <= m:
            res += max(m-h[i], 0)
            i += 1
        elif h[j] <= m:
            j -= 1
            res += max(m-h[j], 0)
        else:
            m = min(h[i], h[j])
    return res


class TestTrappingRainWater(unittest.TestCase):
    def test_trap(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
