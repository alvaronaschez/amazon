"""
https://leetcode.com/explore/interview/card/amazon/82/others/3002/

Reverse Integer
Solution
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = x//abs(x)
        x = abs(x)
        result = 0
        while x:
            result = result*10 + x % 10
            x = x//10
        result = sign*result
        if result >= 2**31 or result < -2**31:
            return 0
        return result
