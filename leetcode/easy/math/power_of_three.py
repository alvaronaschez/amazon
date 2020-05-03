"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""
from math import log


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        try:
            return 3**round(log(n, 3)) == n
        except ValueError:
            return False
