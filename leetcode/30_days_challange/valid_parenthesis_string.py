"""
https://leetcode.com/problems/valid-parenthesis-string/

678. Valid Parenthesis String
Medium

Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity
of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""


class Solution:
    """Really interesting exercise"""
    @classmethod
    def checkValidString(cls,
                         s: str,
                         i=0,
                         min_parentheses=0,
                         max_parentheses=0) -> bool:
        """
        O(n)
        inspired by checkValidString_first_aproach
        """
        if i == len(s):
            return not min_parentheses
        elif s[i] == "(":
            return cls.checkValidString(s, i + 1, min_parentheses + 1,
                                        max_parentheses + 1)
        elif s[i] == ")":
            return max_parentheses and cls.checkValidString(
                s, i + 1, max(0, min_parentheses - 1), max_parentheses - 1)
        elif s[i] == "*":
            return cls.checkValidString(s, i + 1, max(0, min_parentheses - 1),
                                        max_parentheses + 1)

    @classmethod
    def checkValidString_first_aproach(cls,
                                       s: str,
                                       i=0,
                                       parentheses=0) -> bool:
        """O(n³)"""
        if i == len(s):
            return not parentheses
        elif s[i] == "(":
            return cls.checkValidString(s, i + 1, parentheses + 1)
        elif s[i] == ")":
            return parentheses and cls.checkValidString(
                s, i + 1, parentheses - 1)
        elif s[i] == "*":
            return (cls.checkValidString(s, i + 1, parentheses + 1)
                    or parentheses
                    and cls.checkValidString(s, i + 1, parentheses - 1)
                    or cls.checkValidString(s, i + 1, parentheses))
