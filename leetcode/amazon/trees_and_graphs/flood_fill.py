"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2987/

Flood Fill
Solution
An image is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column)
of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color as the starting pixel), and so on. Replace the color
of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected
by a path of the same color as the starting pixel are colored with the new
color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc <
image[0].length.
The value of each color in image[i][j] and newColor will be an integer in
[0, 65535].
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  new_color: int) -> List[List[int]]:
        image = image[:]
        height, width = len(image), len(image[0])
        old_color = image[sr][sc]
        if new_color == old_color:
            return image

        def adjacents(i, j):
            if i - 1 >= 0:
                yield i - 1, j
            if j - 1 >= 0:
                yield i, j - 1
            if i + 1 < height:
                yield i + 1, j
            if j + 1 < width:
                yield i, j + 1

        stack = [(sr, sc)]
        visited = set(stack)
        image[sr][sc] = new_color
        while stack:
            pixel = stack.pop()
            for adj in adjacents(*pixel):
                if adj not in visited:
                    r, c = adj
                    if image[r][c] == old_color:
                        image[r][c] = new_color
                        stack.append(adj)
                    visited.add(adj)
        return image
