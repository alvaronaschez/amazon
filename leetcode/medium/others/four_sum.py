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
