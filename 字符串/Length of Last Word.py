# -*- coding: utf-8 -*-
# @Time : 2021/5/20 9:57
# @Author : haojie zhang

from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lens = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if lens == 0:
                    continue
                break
            lens += 1
        return lens


s = 'a bcd'
obj = Solution()
print(obj.lengthOfLastWord(s))



