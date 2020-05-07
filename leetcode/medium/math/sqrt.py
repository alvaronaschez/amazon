"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/

Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    """binary search"""

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        m = 1
        while m**2 < x:
            m *= 2
        n = m//2
        while n+1 < m:
            y = (n+m)//2
            if y**2 == x:
                return y
            elif y**2 < x:
                n = y
            else:
                m = y
        return m if m**2 == x else n
