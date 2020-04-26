"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2984/

Lowest Common Ancestor of a Binary Tree
Solution
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
from typing import Tuple


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """iterative solution"""
    parents = {root: None}
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            parents[node.left] = node
            parents[node.right] = node
            stack.append(node.left)
            stack.append(node.right)
            if p in parents and q in parents:
                break
    p_parents = [p]
    q_parents = [q]
    while p:= parents[p]: # noqa (walrus)
        p_parents.append(p)
    while q:= parents[q]: # noqa (walrus)
        q_parents.append(q)
    for n1, n2 in zip(reversed(p_parents), reversed(q_parents)):
        if n1 == n2:
            result = n1
    return result


class Solution:
    """recursive solution"""
    @classmethod
    def lowestCommonAncestorRecursive(
            cls, root: TreeNode, p: TreeNode, q: TreeNode
            ) -> Tuple[bool, bool, TreeNode]:
        """aux recursive function"""
        if not root:
            return False, False, None
        a, b, c = cls.lowestCommonAncestorRecursive(root.left, p, q)
        if a and b:
            return a, b, c
        if (a or b) and root in (p, q):
            return True, True, root
        x, y, z = cls.lowestCommonAncestorRecursive(root.right, p, q)
        if x and y:
            return x, y, z
        if (x or y) and root in (p, q):
            return True, True, root
        return (
            a or x or root == p,
            b or y or root == q,
            root if (a or x) and (b or y) else None)

    @classmethod
    def lowestCommonAncestor(
            cls, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        *_, result = cls.lowestCommonAncestorRecursive(root, p, q)
        return result
