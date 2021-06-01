# -*- coding: utf-8 -*-
# @Time : 2021/5/29 14:59
# @Author : haojie zhang


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        m = len(s)
        dp = [0] * (m+1)
        dp[0] = True
        f = [[] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, i+1):
                if s[j-1:i] in wordDict and dp[j-1]:
                    dp[i] = True
                    if j == 1:
                        f[i].append(s[j-1:i])
                    else:
                        for v in f[j-1]:
                            f[i].append(v + ' ' + s[j-1:i])
        return f[-1]


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]


obj = Solution()
print(obj.wordBreak(s, wordDict))