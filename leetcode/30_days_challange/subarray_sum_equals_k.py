from typing import List
from collections import defaultdict


class Solution:
    def first_solution(self, nums: List[int], k: int) -> int:
        """
        O(n^2)
        """
        aux = []
        acc = 0
        for num in nums:
            aux.append(acc)
            acc += num
        aux.append(acc)
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if aux[j] - aux[i] == k:
                    result += 1
        return result

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        O(n)
        inspired by the other solution
        """
        acc = 0
        aux = defaultdict(lambda: 0)
        aux[0] += 1
        result = 0
        for num in nums:
            acc += num
            result += aux[acc - k]
            aux[acc] += 1
        return result
