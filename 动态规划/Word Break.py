# -*- coding: utf-8 -*-
# @Time : 2021/5/29 14:48
# @Author : haojie zhang

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        dp = [False] * (m+1)
        dp[0] = True
        for i in range(1, m+1):
            for j in range(1, i+1):
                if s[j-1:i] in wordDict and dp[j-1]:
                    dp[i] = dp[j-1]
                    break
        return dp[-1]


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
obj = Solution()
print(obj.wordBreak(s, wordDict))