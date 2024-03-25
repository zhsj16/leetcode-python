from typing import *

# 遍历s，选和不选两次dfs：
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         n = len(s)
#         path = []
#
#         def dfs(start, i):
#             if i == n:
#                 res.append(path[:])
#                 return
#             if i < n - 1:
#                 dfs(start, i + 1)
#             t = s[start:i + 1]
#             if t == t[::-1]:
#                 path.append(t)
#                 dfs(i + 1, i + 1)
#                 path.pop()
#
#         dfs(0, 0)
#         return res

# 2024.3.25 一次dfs，答案视角，for循环实现：
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path[:])
                return
            else:
                for j in range(i, n):
                    t = s[i:j + 1]  # j+1
                    if t == t[::-1]:
                        path.append(t)
                        dfs(j + 1)
                        path.pop()

        dfs(0)
        return ans