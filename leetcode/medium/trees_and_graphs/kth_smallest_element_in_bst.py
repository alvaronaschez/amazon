r"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/

Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to
find the kth smallest frequently? How would you optimize the kthSmallest
routine?
"""


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def inorder(cls, root):
        if root:
            yield from cls.inorder(root.left)
            yield root.val
            yield from cls.inorder(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        for i, x in enumerate(self.inorder(root), 1):
            if i == k:
                return x
