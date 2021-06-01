# -*- coding: utf-8 -*-
# @Time : 2021/5/21 16:43
# @Author : haojie zhang


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        f = [0] * (n+1)
        dp = [[False] * n for _ in range(n)]
        for i in range(n+1):
            f[i] = n - i - 1
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    f[i] = min(f[i], f[j+1] + 1)

        return f[0]


s = "cdd"
obj = Solution()
print(obj.minCut(s))