# -*- coding: utf-8 -*-
# @Time : 2021/5/19 13:59
# @Author : haojie zhang



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        maxn = 1
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1]):
                    dp[i][j] = dp[i+1][j-1] + 2
                    if dp[i][j] > maxn:
                        start = i
                        maxn = dp[i][j]
                else:
                    dp[i][j] = 0
        return s[start:start+maxn]


s = "babad"
obj = Solution()
print(obj.longestPalindrome(s))