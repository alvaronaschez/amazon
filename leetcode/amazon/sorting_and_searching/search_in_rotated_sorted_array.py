"""
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/2992/

Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List


def search(a: List[int], target: int) -> int:
    # corner cases
    if not a:
        return -1
    if len(a) == 1:
        return -1 if a[0] != target else 0
    # binary search the rotation point
    i = 0
    j = len(a)-1
    m = (i+j)//2
    while j-i > 1:
        if a[i] < a[m]:
            i = m
        else:
            j = m
        m = (i+j)//2
    if a[0] < a[len(a)-1]:
        j, i = 0, len(a)-1
    # i is the index of the max element in the array
    # j is the index of the min element in the array

    # binary search target
    if a[0] <= target:
        i, j = 0, i
    else:
        i, j = j, len(a)-1

    while i <= j:
        m = (i+j)//2
        if a[m] == target:
            return m
        elif target < a[m]:
            j = m-1
        else:
            i = m+1
    return -1
