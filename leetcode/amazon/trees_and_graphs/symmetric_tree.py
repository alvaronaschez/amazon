r"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/507/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.


"""


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric_first(self, root: TreeNode) -> bool:
        """first attempt"""
        def foo(n):
            if not n:
                yield None
                return
            yield n.val
            yield from foo(n.left)
            yield from foo(n.right)

        def bar(n):
            if not n:
                yield None
                return
            yield n.val
            yield from bar(n.right)
            yield from bar(n.left)

        if not root:
            return True
        n1, n2 = root.left, root.right
        for x, y in zip(foo(n1), bar(n2)):
            if x != y:
                return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        """optimization"""
        def foo(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            return n1.val == n2.val and foo(n1.left, n2.right) and foo(n1.right, n2.left)
        if not root:
            return True
        return foo(root.left, root.right)
