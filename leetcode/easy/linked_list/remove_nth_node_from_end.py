"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its
head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end,
the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        aux = head
        node = head
        while node.next:
            i += 1
            if i > n:
                aux = aux.next
            node = node.next
        if i >= n:
            aux.next = aux.next.next
            return head
        else:
            return aux.next
