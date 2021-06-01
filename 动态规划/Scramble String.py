# -*- coding: utf-8 -*-
# @Time : 2021/5/26 14:32
# @Author : haojie zhang

from collections import Counter

from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        def dfs(s1, s2, i, j, n):
            if (i, j, n) in hashMap:
                return hashMap[(i, j, n)]

            if s1[i:i+n] == s2[j:j+n]:
                return True
            if Counter(s1[i:i+n]) != Counter(s2[j:j+n]):
                return False

            for k in range(1, n):
                if dfs(s1, s2, i, j, k) and dfs(s1, s2, i+k, j+k, n-k):
                    hashMap[(i, j, n)] = True
                    return True
                if dfs(s1, s2, i, j+n-k, k) and dfs(s1, s2, i+k, j, n-k):
                    hashMap[(i, j, n)] = True
                    return True

            hashMap[(i, j, n)] = False
            return False

        hashMap = {}
        return dfs(s1, s2, 0, 0, len(s1))


s1 = "great"
s2 = "rgeat"
s = Solution()
print(s.isScramble(s1, s2))


s1 = "abcde"
s2 = "caebd"
print(s.isScramble(s1, s2))

