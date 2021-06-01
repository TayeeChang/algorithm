# -*- coding: utf-8 -*-
# @Time : 2021/6/1 17:13
# @Author : haojie zhang

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0
        last = 0
        step = 0
        for i in range(len(nums)):
            if i > last:
                last = reach
                step += 1
            reach = max(reach, i + nums[i])
        return step

