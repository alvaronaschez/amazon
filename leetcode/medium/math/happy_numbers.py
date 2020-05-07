"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/

Happy Number

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
import unittest


class Solution:
    not_happy = set()

    @classmethod
    def isHappy(cls, n: int) -> bool:
        s = set()
        while n != 1 and n not in cls.not_happy and n not in s:
            s.add(n)
            n = sum(int(dig)**2 for dig in str(n))
        if n != 1:
            cls.not_happy |= s
        return n == 1


class TestHappy(unittest.TestCase):
    def test_happy(self):
        s = Solution()
        self.assertTrue(s.isHappy(10))
        self.assertTrue(s.isHappy(10))


if __name__ == "__main__":
    unittest.main()
