class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        for i in range(len(nums)-1, -1, -1):
            if i==0 or nums[i-1] < nums[i]:
                break
        if i==0:
            nums.sort()
            return
        aux = sorted(nums[i:])
        nums[i:]=aux
        for j in range(i,len(nums)):
            if nums[i - 1] < nums[j]:
                break
        nums[i - 1], nums[j] = nums[j], nums[i - 1]