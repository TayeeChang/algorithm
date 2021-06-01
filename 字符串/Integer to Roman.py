# -*- coding: utf-8 -*-
# @Time : 2021/5/19 16:05
# @Author : haojie zhang


class Solution:
    def intToRoman(self, num: int) -> str:
        radix = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        for i in range(len(radix)):
            cnt = num // radix[i]
            num = num % radix[i]
            for j in range(cnt):
                roman += symbol[i]
        return roman


num = 1994
s = Solution()
print(s.intToRoman(num))
