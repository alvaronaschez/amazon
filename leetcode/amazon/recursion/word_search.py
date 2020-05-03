"""
https://leetcode.com/explore/interview/card/amazon/84/recursion/2989/

Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == word[0]:
                    starts.append((i, j))
        for i, j in starts:
            visited = set()
            if self.foo(board, word, 0, i, j, visited):
                return True
        return False

    def adjs(self, i, j, board):
        if i - 1 >= 0:
            yield i - 1, j
        if j - 1 >= 0:
            yield i, j - 1
        if i + 1 < len(board):
            yield i + 1, j
        if j + 1 < len(board[0]):
            yield i, j + 1

    def foo(self, board, word, idx, i, j, visited):
        if idx == len(word):
            return True
        elif word[idx] != board[i][j]:
            return False
        elif idx + 1 == len(word):
            return True
        else:
            visited.add((i, j))
            for x, y in self.adjs(i, j, board):
                if (x, y) not in visited and self.foo(board, word, idx + 1, x,
                                                      y, visited):
                    return True
            visited.difference_update({(i, j)})
            return False
