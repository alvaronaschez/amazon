"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for x in zip(*strs):
            if len(set(x)) > 1:
                break
            else:
                result.append(x[0])
        return "".join(result)
