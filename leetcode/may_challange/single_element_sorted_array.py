"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element
appears exactly twice, except for one element which appears exactly once.
Find this single element that appears only once.


Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == nums[m + 1]:
                n, m = m - 1, m + 2
            elif nums[m] == nums[m - 1]:
                n, m = m - 2, m + 1
            else:
                return nums[m]
            if n - i + 1 > 0 and (n - i + 1) % 2 == 1:
                j = n
            else:
                i = m
        return nums[i]


s = Solution()
x = s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
print(x)
