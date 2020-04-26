"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/483/

Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from typing import List


def build_path(node):
    word, prev = node
    result = [word]
    while prev:
        word, prev = prev
        result.append(word)
    return reversed(result)


def findLadders(begin: str, end: str, words: List[str]) -> List[List[str]]:
    n = len(begin)
    dictionary = {}
    for word in words:
        for i in range(n):
            dictionary.setdefault(word[:i]+"*"+word[i+1:], []).append(word)
    stack = [(begin, None)]
    closed_set = set()
    result = []
    while stack:
        next_level = []
        while stack:
            current = stack.pop()
            word, _ = current
            closed_set.add(word)
            for i in range(n):
                for neighbor in dictionary.get(word[:i]+"*"+word[i+1:], []):
                    if neighbor == end:
                        result.append((neighbor, current))
                    elif neighbor not in closed_set:
                        next_level.append((neighbor, current))
        if not result:
            stack = next_level
    result = [build_path(node) for node in result]
    return result
