"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from itertools import repeat
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        for i, x in enumerate(nums):
            if x == 0:
                c += 1
            elif c > 0:
                nums[i-c] = nums[i]
        if c:
            nums[-c:] = repeat(0, c)
