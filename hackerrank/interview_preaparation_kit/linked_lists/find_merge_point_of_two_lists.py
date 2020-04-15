"""
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/
"""
# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def findMergeNode(head1, head2):
    s = set()
    while head1:
        s.add(head1)
        head1 = head1.next
    while head2:
        if head2 in s:
            return head2.data
        head2 = head2.next
