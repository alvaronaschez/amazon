"""
https://leetcode.com/explore/interview/card/amazon/81/design/503/

Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""

from collections import defaultdict
from heapq import heappush, heappop
from math import inf


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [inf]

    def push(self, x: int) -> None:
        m = self.min[-1]
        m = min(m, x)
        self.min.append(m)
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


class HeapMinStack:

    """
    this solution passes all testcases but is cheating
    using a heap doesn't do it's job in constant time
    """

    def __init__(self):
        self.dic = defaultdict(lambda: 0)
        self.stack = []
        self.heap = []

    def push(self, x: int) -> None:
        if x not in self.dic:
            heappush(self.heap, x)
        self.dic[x] += 1
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        self.dic[x] -= 1
        if self.dic[x] == 0:
            del self.dic[x]
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        while self.heap[0] not in self.dic:
            heappop(self.heap)
        return self.heap[0]
