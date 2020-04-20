"""
https://leetcode.com/explore/interview/card/amazon/77/linked-list/512/

Merge k Sorted Lists
Solution
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

from functools import reduce
from typing import List
from math import inf
import unittest
from heapq import heappop, heappush


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None

# monkey patch


def lt(self, other):
    return self.val < other.val


ListNode.__lt__ = lt
# end of monkey patch


def mergeKLists(lists: List[ListNode]) -> ListNode:
    """version definitiva"""
    aux = []
    for node in lists:
        while node:
            aux.append(node)
            node = node.next
    aux.sort()
    for n, m in zip(aux, aux[1:]):
        n.next = m
    return None if not aux else aux[0]


# otras versiones anteriores
"""
def argmin(it):
    m = reduce(min, it, inf)
    for i, x in enumerate(it):
        if x == m:
            return i


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    if not lists:
        return None
    i = argmin([n.val for n in lists])
    node = lists[i]
    lists[i] = lists[i].next
    if not lists[i]:
        lists[-1], lists[i] = lists[i], lists[-1]
        node.next = merge_k_lists(lists[:-1])
        return node
    else:
        node.next = merge_k_lists(lists)
        return node


def mergeKLists_old(lists: List[ListNode]) -> ListNode:
    return merge_k_lists([n for n in lists if n])


def mergeKLists_heap(lists: List[ListNode]) -> ListNode:
    # depende del monkey patch
    heap = []
    for node in lists:
        while node:
            heappush(heap, node)
            node = node.next
    head = heappop(heap)
    node = head
    while heap:
        node.next = heappop(heap)
        node = node.next
    return head
"""


class TestMergeKLists(unittest.TestCase):
    def test_merge_k_lists(self):
        # el test no está terminado
        l = [[1, 4, 5], [1, 3, 4], [2, 6]]
        lists = [list(map(ListNode, x)) for x in l]
        for l in lists:
            for n, m in zip(l, l[1:]):
                n.next = m
        lists = [l[0] for l in lists]
        result = mergeKLists(lists)
        while result:
            # print(result.val)
            result = result.next


if __name__ == "__main__":
    unittest.main(verbosity=2)
