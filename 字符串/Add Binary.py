# -*- coding: utf-8 -*-
# @Time : 2021/5/19 13:51
# @Author : haojie zhang


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        n = max(len(a), len(b))
        s = ''
        carry = 0
        for i in range(n):
            num1 = int(a[i]) if i < len(a) else 0
            num2 = int(b[i]) if i < len(b) else 0
            num = (num1 + num2 + carry) % 2
            carry = (num1 + num2 + carry) // 2
            s += str(num)

        if carry:
            s += str(carry)
        return s[::-1]


a = '11'
b = '1'
s = Solution()
print(s.addBinary(a, b))
