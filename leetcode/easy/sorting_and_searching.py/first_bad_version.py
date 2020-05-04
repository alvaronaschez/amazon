"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/

First Bad Version

You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version. You should
minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""
import unittest


FIRST_BAD_VERSION = 5


def isBadVersion(version):
    # The isBadVersion API is already defined for you.
    # @param version, an integer
    # @return a bool

    return version >= FIRST_BAD_VERSION


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        i = 2
        j = n
        while i <= j:
            m = (i+j)//2
            a, b = isBadVersion(m-1), isBadVersion(m)
            if not a and b:
                return m
            elif a and b:
                j = m-1
            else:
                i = m+1
        return -1


class TestFirstBad(unittest.TestCase):
    def test_first_bad(self):
        def isBadVersion(v): return v >= 5
        s = Solution()
        self.assertEqual(s.firstBadVersion(15), 5)


if __name__ == "__main__":
    unittest.main()
