from collections import Counter, defaultdict
from math import inf
import unittest


class Solution:
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        if not t:
            return ""
        c = Counter(t)
        d = defaultdict(lambda: 0)
        x = 0
        y = inf

        n = 0
        i = 0
        j = 0
        while j < len(s) or n == len(t):
            if n == len(t):
                if j - i < y - x:
                    x, y = i, j
                if s[i] in c:
                    d[s[i]] -= 1
                    if d[s[i]] < c[s[i]]:
                        n -= 1
                i += 1
            elif n < len(t) and j < len(s):
                if s[j] in c:
                    if d[s[j]] < c.get(s[j], inf):
                        n += 1
                    d[s[j]] += 1
                j += 1
        if y == inf:
            return ""
        return s[x:y]


class FirstSolution:
    """a little complex"""
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        c = Counter(t)
        d = defaultdict(lambda: 0)
        x = 0
        y = 0
        m = inf

        n = 0
        i = 0
        j = None
        while True:
            while i < len(s) and s[i] not in c:
                i += 1
            if i >= len(s):
                break
            # solo la primera iteración
            if not j:
                j = i
            while j < len(s) and n < len(t):
                if s[j] in c:
                    if d[s[j]] < c[s[j]]:
                        n += 1
                    d[s[j]] += 1
                j += 1
            if n != len(t):
                break
            while s[i] not in c or d[s[i]] > c[s[i]]:
                if s[i] in c:
                    d[s[i]] -= 1
                i += 1
            if j - i < m:
                x, y, m = i, j, j - i
            if j >= len(s):
                break
            # prepare next iteration
            d[s[i]] -= 1
            n -= 1
            i += 1
        return s[x:y]


class TestMinWindow(unittest.TestCase):
    def test_min_window(self):
        self.assertEqual(Solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(FirstSolution.minWindow("ADOBECODEBANC", "ABC"),
                         "BANC")


if __name__ == "__main__":
    unittest.main(verbosity=2)
