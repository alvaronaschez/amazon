"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/817/

Excel Sheet Column Number

Given a column title as appear in an Excel sheet,
return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        base = ord("Z")-ord("A")+1
        for i, c in enumerate(reversed(s)):
            result += (ord(c)-ord("A")+1)*base**i
        return result
