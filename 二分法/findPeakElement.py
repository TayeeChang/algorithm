# -*- coding: utf-8 -*-
# @Time : 2021/4/26 11:36
# @Author : haojie zhang

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low +(high - low) // 2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low


nums = [1, 2, 3, 1]
print(Solution().findPeakElement(nums))