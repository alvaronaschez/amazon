not finoshed yet!

"""from typing import List


def median(nums: List[int]) -> List[int]:
    m = len(nums)//2
    if len(nums) % 2 == 1:
        return nums[m:m+1]
    else:
        return nums[m-1:m+1]


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m1 = median(nums1)
    m2 = median(nums2)
    m = sorted(m1+m2)
    return sum(median(m))/len(m)
"""
