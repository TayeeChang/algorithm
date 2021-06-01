# -*- coding: utf-8 -*-
# @Time : 2021/5/19 14:27
# @Author : haojie zhang


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        # 初始化 s为空, 但是可以成功匹配的情况
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if j >= 2 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]


s = 'aab'
p = 'c*a*b'
obj = Solution()
print(obj.isMatch(s, p))
