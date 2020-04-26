"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2967/

3Sum Closest

Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = inf
        for k, a in enumerate(nums[:-2]):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = a + nums[i] + nums[j]
                if abs(target - s) < abs(target - result):
                    result = s
                if s == target:
                    return s
                elif s < target:
                    i += 1
                else:
                    j -= 1
        return result
