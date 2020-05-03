"""
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/497/

Meeting Rooms II


Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
from typing import List
from heapq import heappush, heappop, heapify


class Solution2c:
    """O(n log n)"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        a = []
        for s, e in intervals:
            a.append((e, 0))
            a.append((s, 1))
        a.sort(reverse=True)
        result = count = 0
        while a:
            _, code = a.pop()
            if code == 0:
                count -= 1
            else:
                count += 1
            result = max(result, count)
        return result


class Solution2b:
    """O(n log n)"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        for s, e in intervals:
            heap.append((e, 0))
            heap.append((s, 1))
        heapify(heap)
        result = count = 0
        while heap:
            _, code = heappop(heap)
            if code == 0:
                count -= 1
            else:
                count += 1
            result = max(result, count)
        return result


class Solution2a:
    """O(n log n)"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        for s, e in intervals:
            heappush(heap, (e, 0))
            heappush(heap, (s, 1))
        result = count = 0
        while heap:
            _, code = heappop(heap)
            if code == 0:
                count -= 1
            else:
                count += 1
            result = max(result, count)
        return result


class Solution1:
    """O(n log n)"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals)
        heap = [intervals[0][1]]
        result = 1
        for (s, e) in intervals[1:]:
            while heap and s >= heap[0]:
                heappop(heap)
            heappush(heap, e)
            result = max(len(heap), result)
        return result


class QuadraticSolution:
    """O(n^2)"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        a = sorted(set((t for interval in intervals for t in interval)))
        a = {t: i for i, t in enumerate(a)}
        intervals = [(a[s], a[e]) for s, e in intervals]
        a = [0]*len(a)
        for s, e in intervals:
            for i in range(s, e):
                a[i] += 1
        return max(a) if a else 0


class Solution_slow:
    """
    timeout in one test
    first aproach, bad solution
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return self.rooms(sorted(intervals, key=lambda x: (x[0], -x[1])))

    def rooms(self, intervals):
        if not intervals:
            return 0
        a = []
        b = []
        x, y = intervals[0]
        for i, j in intervals[1:]:
            if j <= y:
                a.append((i, j))
            elif i < y:
                a.append((i, y))
                b.append((y, j))
            else:
                b.append((i, j))
        return max(1+self.rooms(a), self.rooms(b))
