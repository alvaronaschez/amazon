"""
https://leetcode.com/explore/interview/card/amazon/84/recursion/2990/

Word Search II

Given a 2D board and a list of words from the dictionary, find all words in
the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring. The
same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""
import unittest
from typing import List
from collections import defaultdict


class Trie:
    def __init__(self):
        self.value = None
        self.children = defaultdict(Trie)

    def __getitem__(self, key):
        return self.children.get(key, None)

    def __bool__(self):
        return True

    def add(self, key):
        node = self
        for char in key:
            node = node.children[char]
        node.value = key

    @classmethod
    def from_list(cls, words):
        obj = cls()
        for word in words:
            obj.add(word)
        return obj


class Solution:
    @classmethod
    def findWords(cls, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie.from_list(words)
        result = set()
        starts = ((i, j) for i in range(len(board))
                  for j in range(len(board[0])))
        visited = set()
        for start in starts:
            cls.aux(start, trie, board, visited, result)
        return list(result)

    @classmethod
    def aux(cls, position, trie, board, visited, result):
        i, j = position
        if position not in visited and (trie: = trie[board[i][j]]):  # noqa
            visited.add(position)
            if trie.value:
                result.add(trie.value)
            for neighbor in cls.neighbors(position, board):
                cls.aux(neighbor, trie, board, visited, result)
            visited -= {position}

    @staticmethod
    def neighbors(position, board):
        i, j = position
        for (i, j) in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
            if 0 <= i and 0 <= j and i < len(board) and j < len(board[0]):
                yield i, j


class TestWordSearch(unittest.TestCase):
    def test_word_search(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        self.assertCountEqual(Solution.findWords(
            board, words), ["eat", "oath"])

    def test_no_words(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = []
        self.assertEqual(Solution.findWords(board, words), [])

    def test_no_board(self):
        board = []
        words = ["oath", "pea", "eat", "rain"]
        self.assertEqual(Solution.findWords(board, words), [])


if __name__ == "__main__":
    unittest.main()
