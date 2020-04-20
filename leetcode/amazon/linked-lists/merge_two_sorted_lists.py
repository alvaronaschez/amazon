"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


"""


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """recursive version"""
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeTwoLists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        iterative version
        8'14''
        """
        if not l1:
            return l2
        if not l2:
            return l1
        aux = []
        while l1 and l2:
            if l1.val <= l2.val:
                aux.append(l1)
                l1 = l1.next
            else:
                aux.append(l2)
                l2 = l2.next
        while l1:
            aux.append(l1)
            l1 = l1.next
        while l2:
            aux.append(l2)
            l2 = l2.next
        for n1, n2 in zip(aux, aux[1:]):
            n1.next = n2
        return aux[0]
