# -*- coding: utf-8 -*-
# @Time : 2021/5/17 18:28
# @Author : haojie zhang


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count = [0] * 32
        for i in range(len(nums)):
            for j in range(32):
                if nums[i] & (1 << j):
                    count[j] += 1
                count[j] %= 3
        num = 0
        for i in range(32):
            if count[i]:
                # if i == 31:
                #     num -= 1 << i
                # else:
                num += 1 << i

        return num if count[31] == 0 else ~(num ^ 0xffffffff)


nums = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
s = Solution()
print(s.singleNumber(nums))