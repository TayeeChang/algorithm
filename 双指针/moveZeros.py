# -*- coding: utf-8 -*-
# @Time : 2021/5/10 17:00
# @Author : haojie zhang

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p0 = i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[p0] = nums[i]
                p0 += 1
            i += 1
        while p0 < len(nums):
            nums[p0] = 0
            p0 += 1
        return


nums = [0, 1, 0, 3, 12]
s = Solution()
print(s.moveZeroes(nums))