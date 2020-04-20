"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

***
OJO
***
he tardado 32'
me ha fallado la asignación múltiple siguiente durante 20 minutos:
head, head.next, prev = head.next, prev, head 

explicación abajo
"""


from collections import namedtuple


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    """
    MUCHO OJO que este orden de asignacion no funcionaría:
    head, head.next, prev = head.next, prev, head
    porque en el último nodo de la lista
    al asignar primero head a None
    cuando quieres acceder a head.next para la
    siguiente asignacion da NullPointer
    """
    prev = None
    while head:
        head.next, head, prev = prev, head.next, head
    return prev


def reverseList_oldstyle(head: ListNode) -> ListNode:
    """without using multiple assignment"""
    prev = None
    while head:
        aux = head.next
        head.next = prev
        prev = head
        head = aux
    return prev


ReversedList = namedtuple("ReversedList", ["head", "tail"])


def _reverseList_recursive(head: ListNode) -> ReversedList:
    """aux function for the recursive version"""
    if not head or not head.next:
        return ReversedList(head, head)
    else:
        new_head, tail = _reverseList_recursive(head.next)
        old_head = head
        tail.next = old_head
        old_head.next = None
        return ReversedList(new_head, old_head)


def reverseList_recursive(self, head: ListNode) -> ListNode:
    """recursive version"""
    return _reverseList_recursive(head)[0]


x = ListNode(1)
y = ListNode(2)
x.next = y

print(reverseList(x))
