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
from collections import namedtuple


class Solution:
    """
    O(n)
    """
    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, number in enumerate(numbers):
            if (target - number) in d:
                return [d[target - number], i]
            d[number] = i
        return None


class Solution_old:
    """
    tiempo invertido en el ejercicio: 9'48''
    O(n log n)
    """
    Number = namedtuple("Number", ["value", "index"])

    @classmethod
    def twoSum(cls, nums: List[int], target: int) -> List[int]:
        nums = [cls.Number(n, i) for i, n in enumerate(nums)]
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i].value + nums[j].value
            if s == target:
                return [nums[i].index, nums[j].index]
            elif s < target:
                i += 1
            else:
                j -= 1
        return None


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        expected_result = [0, 2]
        result = Solution.twoSum([2, 11, 7, 15], 9)
        result_old = Solution_old.twoSum([2, 11, 7, 15], 9)
        self.assertEquals(result, expected_result)
        self.assertEquals(result_old, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
