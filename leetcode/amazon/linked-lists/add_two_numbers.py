"""
https://leetcode.com/explore/interview/card/amazon/77/linked-list/513/

Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x=None):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    tail = head
    remainder = 0
    while l1 and l2:
        x = l1.val + l2.val + remainder
        remainder = x//10
        x = x % 10
        tail.next = ListNode(x)
        tail = tail.next
        l1 = l1.next
        l2 = l2.next
    if l2:
        l1 = l2
    while l1:
        x = l1.val + remainder
        remainder = x//10
        x = x % 10
        tail.next = ListNode(x)
        tail = tail.next
        l1 = l1.next
    if remainder:
        tail.next = ListNode(remainder)
    return head.next
