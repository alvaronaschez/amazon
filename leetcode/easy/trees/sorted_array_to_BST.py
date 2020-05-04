r"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

Convert Sorted Array to Binary Search Tree
Solution
Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following
height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int], i=0, j=None) -> TreeNode:
        if j is None:
            j = len(nums)-1
        if i > j:
            return None
        elif i == j:
            return TreeNode(nums[i])
        else:
            m = (i+j)//2
            return TreeNode(
                nums[m],
                self.sortedArrayToBST(nums, i, m-1),
                self.sortedArrayToBST(nums, m+1, j)
            )
