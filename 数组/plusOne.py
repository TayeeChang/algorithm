# -*- coding: utf-8 -*-
# @Time : 2021/5/17 13:50
# @Author : haojie zhang


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            if not carry:
                return digits

        if carry:
            digits.insert(0, carry)
        return digits


digits = [4,3,2,1]
s = Solution()
print(s.plusOne(digits))