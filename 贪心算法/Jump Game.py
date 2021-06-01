# -*- coding: utf-8 -*-
# @Time : 2021/6/1 11:33
# @Author : haojie zhang

from typing import List

# 正向

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reach = 0
        i = 0
        while i <= reach and i < len(nums):
            reach = max(reach, i + nums[i])
            i += 1
        return reach >= len(nums)-1

# 逆向
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        left_most = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= left_most:
                left_most = i
        return left_most == 0