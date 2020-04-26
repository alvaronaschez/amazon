"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2968/

Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().
"""
import re


class Solution:
    """
    Rabin Karp: Constant Time Slice
    O(N)
    I think they have missed that with the modulus fix
    you could have collisions
    they are not checking, if you check that then the worst time
    could be O(NL)
    """
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        N = len(needle)
        if N > len(haystack):
            return -1
        modulus = 2**31
        b = ord("z")-ord("a")+1
        needle = tuple(ord(c) for c in needle)
        haystack = tuple(ord(c) for c in haystack)
        h_needle = h = 0
        for x, y in zip(needle, haystack):
            h_needle = (h_needle*b+x) % modulus
            h = (h*b+y) % modulus
        if h == h_needle:
            return 0
        for i, n in enumerate(haystack[N:], N):
            h = ((h - haystack[i-N]*b**(N-1))*b + n) % modulus
            if h == h_needle:
                if haystack[i-N+1:i+1] == needle:
                    # i think there could be collisions
                    return i-N+1
        return -1


class Solution5:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        """
        same as solution 4 but here the most significant byte is the leftmost
        """
        N = len(needle)
        b = ord("z")-ord("a")+1
        haystack = tuple(ord(c) for c in haystack)
        needle = tuple(ord(c) for c in needle)
        k = sum(n*b**i for i, n in enumerate(reversed(needle)))
        x = sum(n*b**i for i, n in enumerate(reversed(haystack[:N])))
        if k == x:
            return 0
        for i, n in enumerate(haystack[N:], N):
            x = (x - haystack[i-N]*b**(N-1))*b + n
            if k == x:
                return i-N+1
        return -1


class Solution4:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        """
        same as solution 5 but here the most significant byte is the rightmost
        """
        N = len(needle)
        b = ord("z")-ord("a")+1
        haystack = tuple(ord(c) for c in haystack)
        needle = tuple(ord(c) for c in needle)
        k = sum(n*b**i for i, n in enumerate(needle))
        x = sum(n*b**i for i, n in enumerate(haystack[:N]))
        if k == x:
            return 0
        for i, n in enumerate(haystack[N:], N):
            x = (x - haystack[i-N])//b + n*b**(N-1)
            if k == x:
                return i-N+1
        return -1


class Solution3:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution1:
    @staticmethod
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i, c in enumerate(haystack):
            if c == needle[0]:
                if haystack[i:i + len(needle)] == needle:
                    return i
        return -1


class Solution2:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        return m.start() if (m:=re.search(needle, haystack)) else -1 # noqa
