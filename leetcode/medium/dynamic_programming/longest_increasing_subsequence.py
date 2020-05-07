"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/

Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to
return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = []
        for num in nums:
            x = (1, num)
            for val, M in memo:
                if num > M and val+1 >= x[0]:
                    x = (val+1, num)
            memo.append(x)
        return max(memo)[0]
