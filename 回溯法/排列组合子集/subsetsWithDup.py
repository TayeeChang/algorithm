# -*- coding: utf-8 -*-
# @Time : 2021/5/4 14:58
# @Author : haojie zhang

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, index, tmp):

            res.append(tmp)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:  # 去重逻辑
                    continue
                dfs(nums, i + 1, tmp + [nums[i]])

        res = []
        nums.sort()
        dfs(nums, 0, [])
        return res