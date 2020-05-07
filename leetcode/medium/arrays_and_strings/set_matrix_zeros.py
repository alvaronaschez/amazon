"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.


Example 1:

Input:

[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:

[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:

[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # replace zeros by None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        # do the rows
        for i, row in enumerate(matrix):
            if None in row:
                for j, x in enumerate(row):
                    if x is not None:
                        matrix[i][j] = 0
        # do the columns
        for j in range(n):
            # false if the column had no zeros
            z = False
            for i in range(m):
                if matrix[i][j] is None:
                    z = True
                    break
            if z:
                for i in range(m):
                    if matrix[i][j] is not None:
                        matrix[i][j] = 0
        # undo replace zeros by None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
