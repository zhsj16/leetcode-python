from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if j != i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                dfs(j + 1, remain - candidates[j])
                path.pop()

        dfs(0, target)
        return res
