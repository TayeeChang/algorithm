# -*- coding: utf-8 -*-
# @Time : 2021/5/24 15:26
# @Author : haojie zhang

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def traceback(s, index):
            if index == len(s):
                return [[]]
            if s[index:] in hashMap:
                return hashMap[s[index:]]

            res = []
            for i in range(index, len(s)):
                t = s[index:i+1]
                if t == t[::-1]:
                    curr = traceback(s, i+1)
                    res += [[t] + v for v in curr]

            hashMap[s[index:]] = res
            return res

        hashMap = {}
        return traceback(s, 0)


s = "aab"
obj = Solution()
print(obj.partition(s))