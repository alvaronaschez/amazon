from typing import List
from math import inf


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        aux = [inf] * len(grid[0])
        aux.append(0)
        for _, row in enumerate(grid):
            for j, num in enumerate(row):
                aux[j] = num + min(aux[j - 1], aux[j])
            aux[-1] = inf
        return aux[-2]


s = Solution()
assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
