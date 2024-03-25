from typing import List


# dfs两次，遍历给定的全集，选与不选：
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         path = []
#         def dfs(path, i):
#             if i == n:
#                 res.append(path[:])
#                 return
#             dfs(path, i+1)
#             path.append(nums[i])
#             dfs(path, i+1)
#             path.pop()
#         dfs(path, 0)
#         return res

# 2024.3.25 dfs函数里dfs一次，答案视角，用for循环实现。

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i):
            ans.append(path[:])
            # i==n时候也要加，此时为全集。
            if i == n:
                return
            else:
                for j in range(i, n):
                    path.append(nums[j])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans
