"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/

Increasing Triplet Subsequence
Given an unsorted array return whether an increasing subsequence of length 3
exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space
complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""
from math import inf
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        def min_before(nums):
            m = inf
            for num in nums:
                yield m
                m = min(m, num)

        def second_min_before(nums):
            m = inf
            for num, n in zip(nums, min_before(nums)):
                yield m
                if num > n and num < m:
                    m = num
        for x, y in zip(second_min_before(nums), nums):
            if x < y:
                return True
        return False
