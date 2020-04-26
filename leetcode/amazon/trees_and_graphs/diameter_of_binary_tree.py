r"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2985/

Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the
tree.The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of
edges between them.
"""

from typing import Tuple


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @classmethod
    def diameter(cls, root: TreeNode) -> Tuple[int, int]:
        if not root:
            return -1, 0
        depth_left, diameter_left = cls.diameter(root.left)
        depth_right, diameter_right = cls.diameter(root.right)
        depth = max(depth_left, depth_right) + 1
        diameter = max(diameter_left, diameter_right,
                       depth_left + depth_right + 2)
        return depth, diameter

    @classmethod
    def diameterOfBinaryTree(cls, root: TreeNode) -> int:
        _, result = cls.diameter(root)
        return result
