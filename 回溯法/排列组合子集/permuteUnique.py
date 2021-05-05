# -*- coding: utf-8 -*-
# @Time : 2021/5/4 14:50
# @Author : haojie zhang

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: # 去重逻辑
                    continue
                dfs(nums[:i]+nums[i+1:], tmp+[nums[i]])
        res = []
        nums.sort()
        dfs(nums, [])
        return res


nums = [1, 1, 2]
s = Solution()
print(s.permuteUnique(nums))