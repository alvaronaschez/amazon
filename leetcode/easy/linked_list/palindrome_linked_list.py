"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
from collections import deque


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()
        while head:
            q.append(head.val)
            head = head.next
        while q:
            try:
                if q.pop() != q.popleft():
                    return False
            except IndexError:
                pass
        return True
