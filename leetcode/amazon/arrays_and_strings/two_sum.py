"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/508/

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

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
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                return [i, j]
            elif s < target:
                i += 1
            else:
                j -= 1
        return None


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        expected_result = [0, 1]
        result = Solution().twoSum([2, 11, 7, 15], 9)
        self.assertEquals(result, expected_result)


if __name__ == "__main__":
    unittest.main()
