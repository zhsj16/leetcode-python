from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []
        path = []

        def dfs(i, remain):
            d = k - len(path)
            if d == 0 and remain == 0:
                ans.append(path[:])
                return
            else:
                if remain < 0 or remain > (2 * i - d + 1) * d / 2:
                    # 递减的数列 i, i-1, ..., i-d+1
                    return
                if i < d:  # 等同于 for j in range(i, d-1, -1):
                    return
                else:
                    for j in range(i, 0, -1):
                        # 不倒叙，上边剪枝无法判断。
                        # 正序，可以不剪枝。
                        path.append(j)
                        dfs(j - 1, remain - j)
                        path.pop()

        dfs(9, n)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))
