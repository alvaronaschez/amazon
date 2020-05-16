"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [num if num else -1 for num in nums]
        result = 0
        d = {0: 0}
        acc = 0
        for i, num in enumerate(nums, 1):
            acc += num
            result = max(result, i - d.setdefault(acc, i))
        return result
