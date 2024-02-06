from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, remain):
            if not remain:
                res.append(path[:])
                return
            for j in range(i, n):
                if remain < candidates[j]:
                    break
                path.append(candidates[j])
                dfs(j, remain - candidates[j])
                path.pop()

        dfs(0, target)
        return res
