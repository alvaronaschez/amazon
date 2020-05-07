"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/

Subsets

Given a set of distinct integers, nums, return all possible
subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)+1):
            result.extend((list(combination)
                           for combination in combinations(nums, i)))
        return result
