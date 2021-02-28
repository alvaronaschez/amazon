"""
Construct Binary Search Tree from Preorder Traversal
Solution
Return the root node of a binary search tree that matches the given preorder
traversal.

(Recall that a binary search tree is a binary tree where for every node, any
descendant of node.left has a value < node.val, and any descendant of
node.right has a value > node.val.  Also recall that a preorder traversal
displays the value of the node first, then traverses node.left, then traverses
node.right.)

It's guaranteed that for the given test cases there is always possible to find
a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]


Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""
from typing import List


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        stack = []
        preorder = list(reversed(preorder))
        node = root = TreeNode(preorder.pop())
        while preorder:
            if preorder[-1] < node.val:
                stack.append(node)
                node.left = TreeNode(preorder.pop())
                node = node.left
            elif not stack or stack[-1].val > preorder[-1]:
                node.right = TreeNode(preorder.pop())
                node = node.right
            else:
                node = stack.pop()
        return root

    def bstFromPreorder_first_solution(self,
                                       preorder: List[int],
                                       i=0,
                                       j=None) -> TreeNode:
        """O(nlogn)"""
        if j is None:
            j = len(preorder) - 1
        if i > j:
            return None
        if i == j:
            return TreeNode(preorder[i])
        pivot = preorder[i]
        i += 1
        s, e = i, j
        while i < j:
            m = (i + j) // 2
            if preorder[m] < pivot:
                i = m + 1
            else:
                j = m
        if preorder[i] > pivot:
            n, m = i - 1, i
        else:
            n, m = i, i + 1
        root = TreeNode(pivot, self.bstFromPreorder(preorder, s, n),
                        self.bstFromPreorder(preorder, m, e))
        return root


"""
s = Solution()
result = s.bstFromPreorder([[8,5,1,7,10,12])
assert result == [8, 5, 10, 1, 7, None, 12]
"""
