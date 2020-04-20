"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2**31 − 1) or INT_MIN (−2**31) is returned.
"""
import unittest
from collections import namedtuple
import re


class Solution:

    INT_MAX = 2**31-1
    INT_MIN = -(2**31)
    DIGITS = frozenset("0123456789")
    SIGN = "+-"

    def myAtoi(self, st: str) -> int:
        """
        15'32'' until first working version (before refactoring)
        """
        # remove leading and trailing spaces
        st = st.strip()
        i = 0
        # skip the sign
        if i < len(st) and st[i] in self.SIGN:
            i += 1
        # skip the digits
        while i < len(st) and st[i] in self.DIGITS:
            i += 1
        # obtain the part with an optional leading sign followed by digits
        st = st[:i]
        # try the conversion: better ask for forgiveness than permission
        try:
            n = int(st)
        except:
            return 0
        # if it's out of range return the indicated number
        if n > self.INT_MAX:
            return self.INT_MAX
        elif n < self.INT_MIN:
            return self.INT_MIN
        else:
            return n

    def myAtoy_re(self, st: str) -> int:
        """
        much simpler version using regular expressions
        """
        m = re.search(r' *[+-]?\d+', st)
        try:
            result = int(m.group(0))
        except:
            return 0
        else:
            result = min(result, self.INT_MAX)
            result = max(result, self.INT_MIN)
            return result


TestCase = namedtuple("TestCase", ["input", "output", "explanation"])


class TestAtoi(unittest.TestCase):
    my_test_cases = [
        TestCase("42", 42, ""),
        TestCase("     -42", -42, "The first non-whitespace character is '-', which is the minus sign."
                 "Then take as many numerical digits as possible, which gets 42."),
        TestCase("4193 with words", 4193,
                 "Conversion stops at digit '3' as the next character is not a numerical digit."),
        TestCase("words and 987", 0, "The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign."
                 "Therefore no valid conversion could be performed."),
        TestCase("-91283472332", -2147483648, "The number '-91283472332' is out of the range of a 32-bit signed integer."
                 "Thefore INT_MIN (−2**31) is returned."),
    ]

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_atoi(self):
        for tc in self.my_test_cases:
            self.assertEqual(self.s.myAtoi(tc.input),
                             tc.output, tc.explanation)

    def test_atoi_re(self):
        for tc in self.my_test_cases:
            self.assertEqual(self.s.myAtoi(tc.input),
                             tc.output, tc.explanation)


if __name__ == '__main__':
    unittest.main(verbosity=2)
