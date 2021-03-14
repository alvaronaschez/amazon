// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
// Given the head of a sorted linked list, delete all nodes that have 
// duplicate numbers, leaving only distinct numbers from the original list.
// Return the linked list sorted as well.

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
    let counter = {};
    while (head) {
        counter[head.val] = counter[head.val] + 1 || 1;
        head = head.next;
    }
    let arr = []
    for (let key in counter) {
        if (counter[key] == 1) {
            arr.push(key);
        }
    }
    head = null;
    for (let e of Array.from(arr).sort((x, y) => x - y).reverse()) {
        head = new ListNode(e, head);
    }
    return head;
};