from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        path = []
        def dfs(path, i):
            if i == n:
                res.append(path[:])
                return
            dfs(path, i+1)
            path.append(nums[i])
            dfs(path, i+1)
            path.pop()
        dfs(path, 0)
        return res
