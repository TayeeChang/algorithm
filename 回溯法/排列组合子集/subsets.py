# -*- coding: utf-8 -*-
# @Time : 2021/5/4 14:52
# @Author : haojie zhang


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def traceback(nums, index, tmp):
            res.append(tmp)
            for i in range(index, len(nums)):
                traceback(nums, i+1, tmp+[nums[i]])

        res = []
        traceback(nums, 0, [])
        return res


nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))