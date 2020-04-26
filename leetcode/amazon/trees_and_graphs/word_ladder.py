"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2982/


Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import defaultdict, deque
from typing import List


def ladderLength(begin: str, end: str, words: List[str]) -> int:
    n = len(begin)
    dictionary = defaultdict(list)
    for word in words:
        for i in range(n):
            dictionary[word[:i]+"*"+word[i+1:]].append(word)
    queue = deque([(begin, 1)])
    closed_set = {begin}
    while queue:
        word, level = queue.pop()
        if end == word:
            return level
        level += 1
        for i in range(n):
            for neighbor in dictionary[word[:i]+"*"+word[i+1:]]:
                if neighbor not in closed_set:
                    closed_set.add(neighbor)
                    queue.appendleft((neighbor, level))
    return 0
