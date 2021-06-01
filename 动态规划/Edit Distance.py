# -*- coding: utf-8 -*-
# @Time : 2021/5/26 15:07
# @Author : haojie zhang


from typing import List
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[-1][-1]
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [i for i in range(n+1)]
        for i in range(1, m+1):
            upper_left = dp[0]
            dp[0] = i
            for j in range(1, n+1):
                upper = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = upper_left
                else:
                    dp[j] = min(dp[j-1], dp[j], upper_left) + 1
                upper_left = upper
        return dp[-1]


word1 = "horse"
word2 = "ros"
s = Solution()
print(s.minDistance(word1, word2))



