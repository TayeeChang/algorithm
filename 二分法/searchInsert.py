# -*- coding: utf-8 -*-
# @Time : 2021/4/26 14:37
# @Author : haojie zhang

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    # 使用左插法
    def lower_bound(self, nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

