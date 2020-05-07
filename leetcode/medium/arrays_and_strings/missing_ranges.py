"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/782/

Missing Ranges
Given a sorted integer array nums, where the range of elements are in the
inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
from typing import List


class Solution:
    @staticmethod
    def gen(nums, lower, upper):
        if not nums:
            yield (lower, upper)
            return
        if nums[0] > lower:
            yield (lower, nums[0]-1)
        yield from ((x+1, y-1) for x, y in zip(nums, nums[1:]) if x+1 < y)
        if nums[-1] < upper:
            yield (nums[-1]+1, upper)

    @classmethod
    def findMissingRanges(cls, nums: List[int],
                          lower: int, upper: int) -> List[str]:
        return [(str(x) if x == y else f"{x}->{y}")
                for x, y in cls.gen(nums, lower, upper)]
