"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/499/

Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not
count as extra space for the purpose of space complexity analysis.)
"""
from operator import mul
from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = sum((1 for num in nums if num == 0))
        if num_zeros > 1:
            return [0] * len(nums)
        prod = reduce(mul, (num for num in nums if num != 0))
        if num_zeros == 1:
            return [prod if num == 0 else 0 for num in nums]
        else:
            return [prod // num for num in nums]
