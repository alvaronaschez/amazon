"""
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/2993/

Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals = sorted(intervals)
        new_intervals = [intervals[0]]
        intervals = (tuple(interval) for interval in intervals[1:])
        for interval in intervals:
            if new_intervals[-1][1] >= interval[0]:
                new_intervals[-1][-1] = max(new_intervals[-1][1], interval[1])
            else:
                new_intervals.append(list(interval))
        return new_intervals
