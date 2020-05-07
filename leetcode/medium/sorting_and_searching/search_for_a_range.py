"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/

Search for a Range

Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect_left(nums, target)
        j = bisect_right(nums, target) - 1
        try:
            if nums[i] == target:
                return [i, j]
        except IndexError:
            pass
        return [-1, -1]
