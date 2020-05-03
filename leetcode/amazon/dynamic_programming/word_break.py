"""
https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/2997/

Word Break

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple
pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
import unittest
from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        if not word_dict:
            return False
        a = sorted(set((len(word) for word in word_dict)))
        word_dict = set(word_dict)
        stack = [0]
        visited = set()
        while stack:
            i = stack.pop()
            if i == len(s):
                return True
            visited.add(i)
            for k in a:
                j = k+i
                if j not in visited and s[i:j] in word_dict:
                    stack.append(j)
        return False


class Trie:
    def __init__(self):
        self.value = None
        self.children = defaultdict(Trie)

    def __getitem__(self, key):
        return self.children[key] if key in self.children else None

    def insert(self, word):
        node = self
        for c in word:
            node = node.children[c]
        node.value = word

    def __bool__(self):
        return True

    @classmethod
    def from_list(cls, words):
        obj = cls()
        for word in words:
            obj.insert(word)
        return obj


class SolutionTrie:
    """too slow"""
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        trie = Trie.from_list(word_dict)
        stack = [(0, trie)]
        while stack:
            i, t = stack.pop()
            if not t:
                continue
            if t.value:
                if i == len(s):
                    return True
                stack.append((i, trie))
            if i<len(s) and (t:=t[s[i]]): # noqa
                stack.append((i+1, t))
        return False


class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        self.assertTrue(Solution().wordBreak("leetcode", ["leet", "code"]))


if __name__ == "__main__":
    unittest.main()
