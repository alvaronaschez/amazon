r"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2981/

Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

from typing import Tuple
from math import inf


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


r"""
enunciado ambiguo
podría interpretarse que un recorrido válido puede pasar dos veces por un
mismo nodo
ejemplo:
    10
   / \
  9  20
    /  \
   15   7
aquí con la interpretación alternativa la solución sería 61
mientras con la interpretación suya es 54
"""


def max_path_sum(root: TreeNode) -> Tuple[int, int]:
    """
    Time Complexity: O(n)
    because we do n calls to the function with constant time each one
    where n is the number of nodes in the tree
    Space Complexity: O(log n)
    Because the space of the recursive calls in the stack
    """
    if not root:
        return -inf, -inf
    left_connected, left_overall = max_path_sum(root.left)
    right_connected, right_overall = max_path_sum(root.right)
    best_connected = root.val + max(left_connected, right_connected, 0)
    # best overall includes root
    best_overall = root.val + max(left_connected, 0) + max(right_connected, 0)
    # best overall does not include root
    best_overall = max(best_overall, max(left_overall, right_overall))
    return best_connected, best_overall


def maxPathSum(root: TreeNode) -> int:
    return max_path_sum(root)[1]
