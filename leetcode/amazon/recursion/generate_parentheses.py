"""
https://leetcode.com/explore/interview/card/amazon/84/recursion/2988/

Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from functools import lru_cache
from typing import List
from collections import defaultdict


@lru_cache
def parenthesis(n: int) -> List[str]:
    """solution 1"""
    if n == 0:
        return [""]
    result = []
    for k in range(1, n + 1):
        for p1 in parenthesis(k - 1):
            for p2 in parenthesis(n - k):
                result.append("".join(["(", p1, ")", p2]))
    return result


class Solution2:
    """solution 2"""
    parenthesis = defaultdict(list)
    parenthesis[0].append("")

    @classmethod
    def generateParenthesis(cls, n: int) -> List[str]:
        if n not in cls.parenthesis:
            for k in range(1, n + 1):
                for p1 in cls.generateParenthesis(k - 1):
                    for p2 in cls.generateParenthesis(n - k):
                        cls.parenthesis[n].append("".join(["(", p1, ")", p2]))
        return cls.parenthesis[n]
