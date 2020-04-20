"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
import unittest
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    open_set = set()
    for i, row in enumerate(grid):
        for j, island in enumerate(row):
            if int(island):
                open_set.add((i, j))
    i = 0
    while open_set:
        i += 1
        connected = {open_set.pop()}
        while connected:
            x = connected.pop()
            neighbors = {
                (x[0] - 1, x[1]),
                (x[0] + 1, x[1]),
                (x[0], x[1] - 1),
                (x[0], x[1] + 1),
            }
            neighbors &= open_set
            connected |= neighbors
            open_set.difference_update(neighbors)
    return i


class TestNumIslands(unittest.TestCase):
    def test_num_islands(self):
        grid = [
            list("11000"),
            list("11000"),
            list("00100"),
            list("00011"),
        ]
        self.assertEqual(num_islands(grid), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
