"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2970/

Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strings:
            d[tuple(sorted(string))].append(string)
        return list(d.values())
