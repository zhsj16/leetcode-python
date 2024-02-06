from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        path = []

        def dfs(start, i):
            if i == n:
                res.append(path[:])
                return
            if i < n - 1:
                dfs(start, i + 1)
            t = s[start:i + 1]
            if t == t[::-1]:
                path.append(t)
                dfs(i + 1, i + 1)
                path.pop()

        dfs(0, 0)
        return res
