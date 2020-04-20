"""
https://leetcode.com/explore/interview/card/amazon/77/linked-list/2978/

he tardado 11'43''

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
"""


class Node:
    """Definition for a Node."""

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        he tardado 11'43''
        """
        d = {None: None}
        myhead = head
        while myhead:
            d[myhead] = Node(myhead.val)
            myhead = myhead.next
        myhead = head
        while myhead:
            d[myhead].next = d[myhead.next]
            d[myhead].random = d[myhead.random]
            myhead = myhead.next
        return d[head]
