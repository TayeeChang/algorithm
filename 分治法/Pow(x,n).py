# -*- coding: utf-8 -*-
# @Time : 2021/6/1 10:40
# @Author : haojie zhang

"""
xn = xn/2 * xn/2 * xn%2
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            v = power(x, n//2)
            if n % 2:
                return v * v * x
            return v * v
        if n < 0:
            return 1. / power(x, -n)
        return power(x, n)


s = Solution()
n = 2
x = 3
print(s.myPow(x, n))