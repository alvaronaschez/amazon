"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2969/

Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly. DO NOT allocate another 2D matrix and do the
rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
from typing import List
import unittest


def rotate(m: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.

    Es más difícil de lo que parece
    """
    N = len(m)
    for k in range(N // 2):
        for i in range(k, N - k - 1):
            m[k][i], m[i][-1-k], m[-1-k][-1-i], m[-1-i][k] = \
                m[-1-i][k], m[k][i], m[i][-1-k], m[-1-k][-1-i]


class TestRotate(unittest.TestCase):
    def test_rotate(self):
        m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        r1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        r2 = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        rotate(m1)
        rotate(m2)
        self.assertEqual(m1, r1)
        self.assertEqual(m2, r2)


if __name__ == "__main__":
    unittest.main()
