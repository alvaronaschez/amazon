"""
https://leetcode.com/explore/interview/card/amazon/82/others/3005/

Prison Cells After N Days
Solution
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the
following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant,
then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the
row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way:
cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N
days (and N such changes described above.)



Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""
import unittest
from typing import List


class Solution:
    """
    bastante dificil pero interesante
    hay que darse cuenta de que la secuencia hace un ciclo
    """

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def xnor(x, y): return ~(x ^ y)
        x = sum((2**i*x for i, x in enumerate(reversed(cells))))
        n = n % 14
        if n == 0:
            n = 14
        for i in range(n):
            x = xnor(x << 1, x >> 1) & 0b1111110
        return list(format(x, "08b"))


class BitewiseSolution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def xnor(x, y): return ~(x ^ y)
        cells = [str(n) for n in cells]
        x = int("".join(cells), 2)
        for _ in range(n):
            x = xnor(x << 1, x >> 1) & 0b1111110
        return list(bin(x)[2:].zfill(8))


class NaiveSolution:
    """
    naive approach
    time limit exceded
    cells.length = 8
    """

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cells = cells[:]
        for _ in range(n):
            y = cells[0]
            for i in range(1, len(cells)-1):
                cells[i], y = 1 if y == cells[i+1] else 0, cells[i]
            cells[0] = cells[-1] = 0
        return cells


class TestPrison(unittest.TestCase):
    def test_prison(self):
        self.assertEqual(
            Solution().prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7),
            [0, 0, 1, 1, 0, 0, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()
