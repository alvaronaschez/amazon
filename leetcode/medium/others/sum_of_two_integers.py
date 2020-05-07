"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/

Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the
operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum((a, b))
