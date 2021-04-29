# -*- coding: utf-8 -*-
# @Time : 2021/4/29 16:23
# @Author : haojie zhang

from typing import List

"""
无重复，每个数字可以无限重复取
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def traceback(nums, index, target, sums, tmp):
            if target == sums:
                res.append(tmp)
                return

            for i in range(index, len(nums)):
                if sums + nums[i] > target:
                    break
                traceback(nums, i, target, sums+nums[i], tmp+[nums[i]])

        res = []
        candidates.sort()
        traceback(candidates, 0, target, 0,  [])
        return res


candidates = [2, 3, 6, 7]
target = 7
s = Solution()
print(s.combinationSum(candidates, target))