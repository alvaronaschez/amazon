import unittest
from typing import List
from random import randint
from heapq import heapify, heappop


def merge(a: List[int], b: List[int]) -> List[int]:
    """not an efficient version"""
    a, b = a[:], b[:]
    result = []
    while a and b:
        if a[-1] >= b[-1]:
            result.append(a.pop())
        else:
            result.append(b.pop())
    while a:
        result.append(a.pop())
    while b:
        result.append(b.pop())
    result.reverse()
    return result


def mergesort(a: List[int]) -> List[int]:
    if not a or len(a) == 1:
        return a
    m = len(a)//2
    a1 = mergesort(a[:m])
    a2 = mergesort(a[m:])
    return merge(a1, a2)


def _quicksort(a: List[int], start=0, end=None) -> None:
    """sorts a in place, optimized"""
    if end is None:
        end = len(a)-1
    if start >= end:
        return
    pivot = a[start]
    i, j = start+1, end
    while i <= j:
        if a[i] <= pivot:
            i += 1
        else:
            a[i], a[j] = a[j], a[i]
            j -= 1
    a[start], a[j] = a[j], a[start]
    _quicksort(a, start, j-1)
    _quicksort(a, j+1, end)


def quicksort(a: List[int], start=0, end=None) -> List[int]:
    """optimized"""
    a = a[:]
    _quicksort(a)
    return a


def heapsort(a: List[int]) -> List[int]:
    """not optimized"""
    heap = a[:]
    heapify(heap)
    result = []
    while heap:
        result.append(heappop(heap))
    return result


class TestSorting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        n = randint(100, 1000)
        cls.input = [randint(0, 10000) for _ in range(n)]
        cls.output = sorted(cls.input)

    def test_mergesort(self):
        self.assertEqual(mergesort(self.input), self.output)

    def test_quicksort(self):
        self.assertEqual(quicksort(self.input), self.output)

    def test_heapsort(self):
        self.assertEqual(heapsort(self.input), self.output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
