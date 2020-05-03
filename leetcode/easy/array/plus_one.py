"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

Plus One

Given a non-empty array of digits representing a non-negative integer, plus
one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the
number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
from typing import List


class Solution:
    def plus_one(self, digits: List[int], j: int = None) -> List[int]:
        """
        modifies the list in place
        """
        if j is None:
            j = len(digits)-1
        digits[j] = (digits[j]+1) % 10
        if digits[j] == 0:
            if j == 0:
                digits.insert(0, 1)
            else:
                return self.plus_one(digits, j-1)

    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[:]
        self.plus_one(digits)
        return digits
