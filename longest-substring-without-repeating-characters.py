# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import deque


class Solution:
    """
    Given a string, find the length of the longest substring without repeating characters.
    """

    def lengthOfLongestSubstring(self, st: str) -> int:
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


def simple_test():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbbbbbbbbbbbbb") == 1
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3


simple_test()
