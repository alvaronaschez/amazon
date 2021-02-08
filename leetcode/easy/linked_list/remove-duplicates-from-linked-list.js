// https://leetcode.com/problems/remove-duplicates-from-sorted-list/
// Given the head of a sorted linked list, delete all duplicates 
// such that each element appears only once. Return the linked list sorted as well.

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const deleteDuplicates = function (head) {
    let s = new Set();
    while (head) {
        s.add(head.val);
        head = head.next;
    }
    head = null;
    for (let e of Array.from(s).sort((x, y) => x - y).reverse()) {
        head = new ListNode(e, head);
    }
    return head;
};
