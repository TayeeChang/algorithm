# -*- coding: utf-8 -*-
# @Time : 2021/5/19 16:15
# @Author : haojie zhang


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        i = 0
        while i < len(s):
            if i == len(s)-1 or roman[s[i]] >= roman[s[i+1]]:
                num += roman[s[i]]
                i += 1
            else:
                num += roman[s[i+1]] - roman[s[i]]
                i += 2
        return num


s = "MCMXCIV"
obj = Solution()
print(obj.romanToInt(s))

