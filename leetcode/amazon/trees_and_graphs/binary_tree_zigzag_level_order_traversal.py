r"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2980/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

from typing import List


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        result = []
        while q:
            a = [x.val for x in q if x]
            if a:
                result.append(a)
            p = []
            for n in q:
                if n:
                    p.append(n.left)
                    p.append(n.right)
            q = p
        for i, l in enumerate(result):
            if i % 2:
                l.reverse()
        return result
