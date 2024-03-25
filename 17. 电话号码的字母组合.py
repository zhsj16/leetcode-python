from typing import List

MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        n = len(digits)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return
            else:
                for c in MAPPING[int(digits[i])]:
                    path.append(c)
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return ans
