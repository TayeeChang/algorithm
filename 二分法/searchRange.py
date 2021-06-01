# -*- coding: utf-8 -*-
# @Time : 2021/4/26 11:03
# @Author : haojie zhang

from typing import List

"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            low, high = 0, len(nums)
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low

        def upper_bound(nums, target):
            low, high = 0, len(nums)
            while low < high:
                mid = low + (high-low) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low

        low = lower_bound(nums, target)
        if low == len(nums) or nums[low] != target:
            return [-1, -1]
        high = upper_bound(nums, target)
        return [low, high-1]


nums = [1, 2, 2]
target = 2
print(Solution().searchRange(nums, target))
