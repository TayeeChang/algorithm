# -*- coding: utf-8 -*-
# @Time : 2021/5/25 15:46
# @Author : haojie zhang

"""
97. 交错字符串
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。

https://leetcode-cn.com/problems/interleaving-string/
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            dp[0][j] = s2[j-1] == s3[j-1] and dp[0][j-1]
        for i in range(1, m+1):
            dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        return dp[-1][-1]

class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):  # 细节1: dp长度 为 长字符串长度+1
            return self.isInterleave(s2, s1, s3)

        m, n = len(s1), len(s2)
        dp = [False] * (n+1)
        dp[0] = True

        for j in range(1, n+1):
            dp[j] = s2[j-1] == s3[j-1] and dp[j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = (s1[i-1] == s3[i+j-1] and dp[j]) or (s2[j-1] == s3[i+j-1] and dp[j-1])
        return dp[-1]


s1 = "aa"
s2 = "ab"
s3 = "abaa"
s = Solution1()
print(s.isInterleave(s1, s2, s3))