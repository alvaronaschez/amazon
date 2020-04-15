"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/508/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List
import unittest


class Solution:
    """
    tiempo invertido en el ejercicio: 9'48''
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(zip(nums, range(len(nums))))
        i, j = 0, -1
        while True:
            s = nums[i][0]+nums[j][0]
            if s == target:
                return [nums[i][1], nums[j][1]]
            if s < target:
                i += 1
            else:
                j -= 1


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        expected_result = [0, 2]
        result = Solution().twoSum([2, 11, 7, 15], 9)
        self.assertEquals(result, expected_result)


if __name__ == "__main__":
    unittest.main()
