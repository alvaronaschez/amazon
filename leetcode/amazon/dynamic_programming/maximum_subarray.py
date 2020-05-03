"""
https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/899/

Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    """
    O(n)
    accepted
    """
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0]
        for num in nums:
            a.append(num + a[-1])
        total = a[-1]
        for i in range(1, len(a)):
            a[i] = min(a[i], a[i - 1])
        b = [0]
        for num in reversed(nums):
            b.append(b[-1] + num)
        for i in range(1, len(b)):
            b[i] = min(b[i], b[i - 1])
        b.reverse()
        return total - min(x + y for x, y in zip(a, b[1:]))


class QuadraticSolution:
    """
    O(n²)
    not accepcted
    """
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0]
        for num in nums:
            a.append(a[-1] + num)
        total = a[-1]
        b = [0]
        for num in reversed(nums):
            b.append(b[-1] + num)
        b.reverse()
        result = total
        for i, n in enumerate(a):
            for m in b[i + 1:]:
                result = max(result, total - n - m)
        return result
