"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/791/

Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of
that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.



Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return
value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer
is null.


Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @classmethod
    def inorder(cls, root):
        if root:
            yield from cls.inorder(root.left)
            yield root
            yield from cls.inorder(root.right)

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        it = iter(self.inorder(root))
        try:
            while True:
                if p == next(it):
                    return next(it)
        except StopIteration:
            return None
