"""
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/482/

Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import unittest
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    return sorted(nums)[-k]


class TestFindKthLargest(unittest.TestCase):
    def test_find_kth_largest(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        output = 4
        self.assertEqual(find_kth_largest(nums, k), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
