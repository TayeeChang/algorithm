# -*- coding: utf-8 -*-
# @Time : 2021/6/2 14:42
# @Author : haojie zhang


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], tmp+[nums[i]])

        res = []
        dfs(nums, [])
        return res


s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))