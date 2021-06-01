# -*- coding: utf-8 -*-
# @Time : 2021/5/19 13:42
# @Author : haojie zhang


class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        i = 0
        sign = 1
        n = len(s)
        INT_MAX = 2 ** 31 - 1
        INT_MIN= - 2 ** 31
        while i < n and s[i] == ' ':
            i += 1
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        for j in range(i, n):
            if not s[j].isdigit():
                break
            num = num * 10 + int(s[j])
        num *= sign
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num
