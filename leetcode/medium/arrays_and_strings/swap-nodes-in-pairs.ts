
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}


function swapPairs(head: ListNode | null): ListNode | null {
    let result = head?.next || head;
    let prev = new ListNode(0, head);
    while (prev.next && prev.next.next) {
        let n1 = prev.next;
        let n2 = prev.next.next;
        prev.next = n2;
        n1.next = n2.next;
        n2.next = n1;
        prev = n1;
    }
    return result;
};