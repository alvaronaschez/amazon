"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/826/

Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital
letters A to Z where different letters represent different tasks. Tasks could
be done without original order. Each task could be done in one interval. For
each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two
same tasks, there must be at least n intervals that CPU are doing different
tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish
all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
import unittest
from typing import List
from collections import Counter, defaultdict, deque
from math import inf
from heapq import heapify, heappush, heappop


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        c = Counter(tasks)
        active = len(c)
        queue = deque([None] * n)
        heap = [[-y, x] for x, y in c.most_common()]
        heapify(heap)
        result = 0
        while heap or active:
            print(queue)
            if heap:
                task = heappop(heap)
                task[0] += 1
                print(task)
                if task[0] == 0:
                    active -= 1
                    task = None
                queue.append(task)
                if x := queue.popleft():  # noqa
                    heappush(heap, x)
            else:
                if x := queue.popleft():  # noqa
                    heappush(heap, x)
                queue.append(None)
            result += 1
        return result


class TestScheduler(unittest.TestCase):
    def test_scheduler(self):
        s = Solution()
        self.assertEqual(
            s.leastInterval(
                ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
            ),
            16,
        )


if __name__ == "__main__":
    unittest.main()
