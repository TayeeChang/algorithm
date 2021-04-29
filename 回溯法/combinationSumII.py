# -*- coding: utf-8 -*-
# @Time : 2021/4/29 16:38
# @Author : haojie zhang

from typing import List

"""
有重复，每个数字只可以使用一次；结果需要去重
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def traceback(nums, index, target, sums, tmp):
            if target == sums:
                res.append(tmp)
                return

            for i in range(index, len(nums)):
                if sums + nums[i] > target:
                    break
                if i > index and nums[i] == nums[i-1]:  # 去重
                    continue
                traceback(nums, i+1, target, sums+nums[i], tmp+[nums[i]])

        res = []
        candidates.sort()
        traceback(candidates, 0, target, 0, [])
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))