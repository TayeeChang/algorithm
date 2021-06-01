# -*- coding: utf-8 -*-
# @Time : 2021/5/25 16:57
# @Author : haojie zhang

"""
516. 最长回文子序列
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1]):
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]

s = "bbbab"
obj = Solution()
print(obj.longestPalindromeSubseq(s))