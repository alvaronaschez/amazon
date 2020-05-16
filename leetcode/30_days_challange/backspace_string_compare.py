"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/

Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution:
    @staticmethod
    def read(s):
        d = 0
        aux = []
        for c in reversed(s):
            if c == "#":
                d += 1
            elif d == 0:
                aux.append(c)
            else:
                d -= 1
        aux.reverse()
        return "".join(aux)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.read(S) == self.read(T)
