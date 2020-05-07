"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/

Search a 2D Matrix II
Solution
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:
    @classmethod
    def binary_search(cls, a, x, i=0, j=None):
        if j is None:
            j = len(a)-1
        if i <= j:
            m = (i+j)//2
            if a[m] == x:
                return True
            elif a[m] > x:
                j = m-1
            else:
                i = m+1
            return cls.binary_search(a, x, i, j)
        else:
            return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False
