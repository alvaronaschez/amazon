"""
3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
from typing import List
from collections import Counter


def naive_three_sum(nums: List[int]) -> List[List[int]]:
    """
    naive solution
    O(n**3)
    """
    result = set()
    for i, a in enumerate(nums):
        for j, b in enumerate(nums[i+1:], i+1):
            for c in nums[j+1:]:
                if a+b+c == 0:
                    result.add(tuple(sorted([a, b, c])))
    return [list(x) for x in result]


def quadratic_three_sum(nums: List[int]) -> List[List[int]]:
    """
    second attempt
    O(n**2)
    """
    c = dict(Counter(nums))
    result = set()
    for i, a in enumerate(nums):
        c[a] -= 1
        for b in nums[i+1:]:
            c[b] -= 1
            if c.get(-a-b, 0):
                result.add(tuple(sorted([a, b, -a-b])))
        for b in nums[i+1:]:
            c[b] += 1
    return [list(x) for x in result]


def three_sum(nums: List[int]) -> List[List[int]]:
    c = dict(Counter(nums))
    for key, value in c.items():
        c[key] = min(value, 3)
    result = []
    keys = sorted(c.keys())
    for i, a in enumerate(keys):
        c[a] -= 1
        for b in keys[i:]:
            if c[b]:
                c[b] -= 1
                if c.get(-a-b, 0) and b <= -a-b:
                    result.append([a, b, -a-b])
                c[b] += 1
        c[a] += 1
    return result


class Solution:
    """
    based on two sum
    O(n**2)
    """

    def twoSum(self, nums: List[int], goal: int) -> List[List[int]]:
        i, j = 0, len(nums)-1
        results = []
        while i < j:
            if nums[i]+nums[j] == goal:
                x = [nums[i], nums[j]]
                if not results or x != results[-1]:
                    results.append(x)
                i += 1
                j -= 1
            elif nums[i]+nums[j] < goal:
                i += 1
            else:
                j -= 1
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        aux = []
        for k, v in Counter(nums).items():
            for i in range(min(v, 3)):
                aux.append(k)
        aux = sorted(aux)
        for i, num in enumerate(aux[:-2]):
            for x in self.twoSum(aux[i+1:], -num):
                result.add(tuple([num]+x))
        return [list(x) for x in result]


# print(three_sum([0, -1, 1]))
