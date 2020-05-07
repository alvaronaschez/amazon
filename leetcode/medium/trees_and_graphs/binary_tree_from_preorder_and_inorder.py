r"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/

Construct Binary Tree from Preorder and Inorder Traversal
Solution
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """not optimized version"""

    def foo(self, preorder, inorder):
        if preorder:
            val = preorder[0]
            j = inorder.index(val)
            len_left = j
            # len_right = len(preorder)-j-1

            preorder_left = preorder[1:1+len_left]
            inorder_left = inorder[:len_left]
            preorder_right = preorder[1+len_left:]
            inorder_right = inorder[1+len_left:]

            return TreeNode(
                val,
                self.foo(preorder_left, inorder_left),
                self.foo(preorder_right, inorder_right)
            )

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.foo(preorder, inorder)
