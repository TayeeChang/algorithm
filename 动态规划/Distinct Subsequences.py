# -*- coding: utf-8 -*-
# @Time : 2021/5/27 17:47
# @Author : haojie zhang

"""

"""
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i-1][j]
        return dp[-1][-1]
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        dp = [0] * (n+1)
        for i in range(1, m+1):
            dp[0] = 1
            for j in range(n, 0, -1):  # dp[i][j] 只跟 dp[i-1][j-1] 和dp[i-1][j]有关 ； 由于有 dp[i-1][j-1]，需要倒着遍历。
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]

        return dp[-1]


s = "babgbag"
t = "bag"
obj = Solution()
print(obj.numDistinct(s, t))

