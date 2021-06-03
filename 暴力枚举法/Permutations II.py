# -*- coding: utf-8 -*-
# @Time : 2021/6/2 14:47
# @Author : haojie zhang

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:], tmp+[nums[i]])

        res = []
        nums.sort()
        dfs(nums, [])
        return res


s = Solution()
nums = [1, 2, 1]
print(s.permuteUnique(nums))