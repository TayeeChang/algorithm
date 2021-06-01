# -*- coding: utf-8 -*-
# @Time : 2021/5/31 14:56
# @Author : haojie zhang

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def traceback(s, index):
            if index in hashMap:
                return hashMap[index]
            if index == len(s):
                return [[]]
            res = []
            for i in range(index, len(s)):
                t = s[index:i+1]
                if t == t[::-1]:
                    res += [[t] + v for v in traceback(s, i+1)]
            hashMap[index] = res
            return res

        hashMap = {}
        traceback(s, 0)
        return hashMap[0]
