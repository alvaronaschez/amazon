r"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/506/

Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from collections import deque
from typing import List


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> List[List[int]]:
    queue = deque([root]) if root else None
    result = []
    while queue:
        result.append([node.val for node in queue])
        aux = deque()
        while queue:
            node = queue.popleft()
            if node.left:
                aux.append(node.left)
            if node.right:
                aux.append(node.right)
        queue = aux
    return result
