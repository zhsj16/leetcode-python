from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i):
            d = k - len(path)
            if d == 0:
                ans.append(path[:])
                return
            else:
                for j in range(i, d - 1, -1):
                    '''
                    怎么理解： 相当于 if i < d: 剪枝
                    想想，i遍历到4，d=3，还要选3个，那还够。
                    如果i已经到2了，最多再选出来1、2，凑不够d=3。
                    这里range右边节点d-1，因为是开区间，所以遍历的j可以取到d，这是正好够的情况。
                    '''
                    path.append(j)
                    dfs(j - 1)
                    path.pop()

        dfs(n)
        '''
        组合型的问题，考虑剪枝的条件：当前池子里剩余的数凑不够了（本题），当前剩余的数的和（216）不够了。
        这两种情况，用倒序更方便。为什么？因为d是剩下需要凑的，倒序正好可以统计当前遍历到1还有多少个数，就是i本身。
        '''
        return ans
