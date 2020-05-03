"""
https://leetcode.com/explore/interview/card/amazon/82/others/3004/

Partition Labels

A string S of lowercase letters is given. We want to partition this string
into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in reversed(range(len(s))):
            if s[i] not in last_index:
                last_index[s[i]] = i
        i = 0
        result = []
        while i < len(s):
            j = i
            length = 0
            while i <= j:
                j = max(j, last_index[s[i]])
                i += 1
                length += 1
            result.append(length)
        return result
