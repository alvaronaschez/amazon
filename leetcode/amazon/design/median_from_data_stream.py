"""
https://leetcode.com/explore/interview/card/amazon/81/design/495/

Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data
structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you
optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would
you optimize it?
"""
from heapq import heappush, heappop


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, x: int):
        heappush(self.heap, x)

    def pop(self):
        return heappop(self.heap)

    def min(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return bool(self.heap)


class MaxHeap(MinHeap):
    def __init__(self):
        super().__init__()

    def push(self, x: int):
        super().push(-x)

    def pop(self):
        return -super().pop()

    def max(self):
        return -super().min()


class MedianFinder:
    def __init__(self):
        self.greater = MinHeap()
        self.less = MaxHeap()
        self.median = None

    def __len__(self):
        return len(self.greater) + len(self.less) + 1 if self.median else 0

    def __bool__(self):
        return bool(self.median is not None or self.greater)

    def addNum(self, x: int) -> None:
        if self.median is not None:
            aux = [self.median, x]
            self.greater.push(max(aux))
            self.less.push(min(aux))
            self.median = None
        elif self:
            aux = sorted([self.greater.pop(), self.less.pop(), x])
            self.greater.push(aux.pop())
            self.median = aux.pop()
            self.less.push(aux.pop())
        else:
            self.median = x

    def findMedian(self) -> float:
        if self.median is not None:
            return self.median
        else:
            return (self.greater.min() + self.less.max()) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
