# -*- coding: utf-8 -*-
# @Time : 2021/6/1 17:44
# @Author : haojie zhang

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] in hashMap and hashMap[s[i]] >= start:
                res = max(res, i-start)
                start = hashMap[s[i]] + 1
            hashMap[s[i]] = i

        return max(res,  len(s) - start)


s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))