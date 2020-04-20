r"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


from math import inf


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def aux(node):
            """18'21'' estoy super cansado, son las 00:20"""
            if not node:
                return True, inf, -inf
            b1, m1, M1 = aux(node.left)
            b2, m2, M2 = aux(node.right)
            b = b1 and b2 and M1 < node.val and m2 > node.val
            return b, min(m1, m2, node.val), max(M1, M2, node.val)
        result, *_ = aux(root)
        return result
