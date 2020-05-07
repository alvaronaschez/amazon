r"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/

Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IterativeSolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        visited = set()
        result = []
        while stack:
            node = stack.pop()
            if node:
                if node in visited:
                    result.append(node.val)
                else:
                    visited.add(node)
                    stack.append(node.right)
                    stack.append(node)
                    stack.append(node.left)
        return result


class RecursiveSolution:
    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root.val
            yield from self.inorder(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return list(self.inorder(root))


class IterativeSolutionLeetcode:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node = root
        result = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
