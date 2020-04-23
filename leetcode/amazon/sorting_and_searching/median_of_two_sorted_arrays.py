"""
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/2991/

Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """O(n log n) porque me iba a volver loco"""
    aux = nums1 + nums2
    aux = sorted(aux)
    return (aux[len(aux)//2]+aux[(len(aux)-1)//2])/2
