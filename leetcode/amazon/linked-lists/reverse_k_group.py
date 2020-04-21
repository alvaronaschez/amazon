"""
https://leetcode.com/explore/interview/card/amazon/77/linked-list/2977/

Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

"""


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # empty list
    if not head:
        return head
    aux = []
    while head:
        aux.append(head)
        head = head.next
    n = len(aux)
    # nothing to reverse
    if k > n:
        return aux[0]
    for i in range(n//k):
        start = i*k
        end = start+k
        # link last element of a group with the first one of the next
        if end+k-1 < n:
            aux[start].next = aux[end+k-1]
        else:
            aux[start].next = aux[end-1].next
        for x, y in zip(aux[start:end], aux[start+1:end]):
            y.next = x
    return aux[k-1]
