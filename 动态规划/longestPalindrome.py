# -*- coding: utf-8 -*-
# @Time : 2021/5/24 11:41
# @Author : haojie zhang

"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

https://leetcode-cn.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        maxn = 1
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = dp[i+1][j-1] + 2
                    if dp[i][j] > maxn:
                        start = i
                        maxn = dp[i][j]
                else:
                    dp[i][j] = 0

        return s[start: start+maxn]

s = "babad"
obj = Solution()
print(obj.longestPalindrome(s))