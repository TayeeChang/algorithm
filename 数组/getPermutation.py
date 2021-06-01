# -*- coding: utf-8 -*-
# @Time : 2021/5/17 10:48
# @Author : haojie zhang

from typing import List

# 康托编码和解码


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        k -= 1
        nums = list(range(1, n+1))
        res = ''

        for i in range(n):
            a = k // fac[n - 1 - i]
            res += str(nums[a])
            nums.pop(a)
            k = k % fac[n - 1 - i]

        return res


n = 3
k = 1
s = Solution()
print(s.getPermutation(n, k))