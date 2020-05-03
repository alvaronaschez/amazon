"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

Pascal's Triangle
Solution
Given a non-negative integer numRows, generate the
first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of
the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangle = [[1]]
        for _ in range(1, numRows):
            triangle.append([1])
            for x, y in zip(triangle[-2], triangle[-2][1:]):
                triangle[-1].append(x + y)
            triangle[-1].append(1)
        return triangle
