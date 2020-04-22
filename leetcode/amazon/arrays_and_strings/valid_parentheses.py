"""

Valid Parentheses
Solution
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


def isValid(s: str) -> bool:
    d = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for c in s:
        if c in d:
            stack.append(c)
        else:
            if not stack or c != d[stack.pop()]:
                return False
    return not stack
