# -*- coding: utf-8 -*-
# @Time : 2021/5/15 22:38
# @Author : haojie zhang

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minv = float('inf')
        res = 0
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low, high = i+1, len(nums)-1
            while low < high:
                sums = nums[i] + nums[low] + nums[high]
                if abs(sums - target) < minv:
                    minv = abs(sums - target)
                    res = sums
                if sums == target:
                    return target
                elif sums < target:
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    low += 1
                else:
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    high -= 1
        return res