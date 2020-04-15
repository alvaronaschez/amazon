"""
https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/
"""

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def reverse(head):
    if head is None:
        return head
    head.prev, head.next = head.next, head.prev
    if head.prev is None:
        return head
    return reverse(head.prev)
