from collections import deque
import unittest


class Solution:
    """
    Given a string, find the length of the longest substring without repeating characters.
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """

    def lengthOfLongestSubstring(self, st: str) -> int:
        """
        tiempo invertido en la solución: 10'40''
        """
        s = set()
        q = deque()
        result = 0
        for c in st:
            if c in s:
                result = max(result, len(q))
                while True:
                    d = q.popleft()
                    s.difference_update({d})
                    if c == d:
                        break
            q.append(c)
            s.add(c)
        return max(result, len(q))

    def lengthOfLongestSubstring_v2(self, st: str) -> int:
        """
        he hecho este ejercicio sin mirar la resolución anterior
        ha salido casi igual, bastante impresionante cómo he programado
        lo mismo con una semana de diferencia y no me acordaba de nada
        tiempo invertido en la solución: 10'40'' 
        (el tiempo realmente corresponde a esta solución, no a la anterior)
        """
        result = 0
        s = set()
        q = deque()
        for c in st:
            if c in s:
                result = max(result, len(s))
                while q:
                    x = q.popleft()
                    s.difference_update({x})
                    if x == c:
                        break
            s.add(c)
            q.append(c)
        return max(result, len(s))


class TestLontestSubstring(unittest.TestCase):
    def test_longest_substring(self):
        s = Solution()
        functions = [s.lengthOfLongestSubstring, s.lengthOfLongestSubstring_v2]
        test_cases = [
            ("abcabcbb", 3),
            ("bbbbbbbbbbbbbbbb", 1),
            ("", 0),
            ("pwwkew", 3),
        ]
        for f in functions:
            for st, expected_result in test_cases:
                self.assertEqual(f(st), expected_result, f.__name__)


if __name__ == '__main__':
    unittest.main(verbosity=2)
