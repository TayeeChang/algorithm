# -*- coding: utf-8 -*-
# @Time : 2021/5/19 14:51
# @Author : haojie zhang


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]  # '*' 匹配空字符串 或者 任意字符串

        return dp[-1][-1]


s = "acdcb"
p = "a*c?b"
obj = Solution()
print(obj.isMatch(s, p))





