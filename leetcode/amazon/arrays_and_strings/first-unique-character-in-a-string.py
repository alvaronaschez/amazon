"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/480/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

import unittest
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        2'45''
        """
        aparences = Counter(s)
        for i, c in enumerate(s):
            if aparences[c] == 1:
                return i
        return -1


class TestFirstUniqChar(unittest.TestCase):
    def test_first_uniq_char(self):
        s = Solution()
        self.assertEqual(s.firstUniqChar("leetcode"), 0)
        self.assertEqual(s.firstUniqChar("loveleetcode"), 2)
        self.assertEqual(s.firstUniqChar("aabbccc"), -1)
        self.assertEqual(s.firstUniqChar(""), -1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
