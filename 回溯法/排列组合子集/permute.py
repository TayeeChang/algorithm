# -*- coding: utf-8 -*-
# @Time : 2021/5/4 14:47
# @Author : haojie zhang

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traceback(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                traceback(nums[:i]+nums[i+1:], tmp+[nums[i]])

        res = []
        traceback(nums, [])
        return res


nums = [1, 2, 3, 4]
s = Solution()
print(s.permute(nums))