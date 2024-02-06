from typing import *


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        path = []
        check = [0] * n

        def dfs(path):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if i > 0 and check[i - 1] == 0 and nums[i] == nums[i - 1]:
                    continue
                if check[i] == 0:
                    check[i] = 1
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                    check[i] = 0

        dfs(path)
        return res
