from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i):
            if len(path) == k:
                ans.append(path[:])
                return
            else:
                for j in range(i, n):
                    path.append(j + 1)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans
