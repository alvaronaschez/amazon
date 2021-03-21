# https://leetcode.com/problems/4sum/

'''
18. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class MyCounter(Counter):
    def __le__(self, other):
        for key, amount in self.items():
            if amount > other[key]:
                return False
        return True


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        c = MyCounter(nums)
        nums = set(nums)
        d = {}
        result = set()
        for n in nums:
            for m in nums:
                d.setdefault(n + m, []).append([n, m])
        for key, value in d.items():
            if target - key in d:
                for r in value:
                    for s in d[target - key]:
                        t = r + s
                        if MyCounter(t) <= c:
                            result.add(tuple(sorted(t)))
        return [list(x) for x in result]
