# -*- coding: utf-8 -*-
# @Time : 2021/6/2 14:09
# @Author : haojie zhang

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, index, tmp):

            if index == len(nums):
                res.append(tmp)
                return

            dfs(nums, index + 1, tmp)  # 不选
            dfs(nums, index+1, tmp+[nums[index]])  # 选


        res = []
        dfs(nums, 0, [])

        return res


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, tmp):
            res.append(tmp)
            for i in range(index, len(nums)):
                dfs(nums, i+1, tmp+[nums[i]])

        res = []
        dfs(nums, 0, [])
        return res


nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))
s1 = Solution1()
print(s1.subsets(nums))