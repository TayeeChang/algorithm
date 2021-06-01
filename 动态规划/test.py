# -*- coding: utf-8 -*-
# @Time : 2021/5/26 10:40
# @Author : haojie zhang


class Solution:
    def numDecodings_(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        n = len(s)
        a, b, c = 0, 1, 0
        for i in range(n):
            c = 0
            if s[i] != '0':
                c += b
            if i >= 1 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                c += a
            a, b = b, c
        return c


s = '12'
obj = Solution()
print(obj.numDecodings1(s))





