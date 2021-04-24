# -*- coding: utf-8 -*-
# @Time : 2021/4/24 19:56
# @Author : haojie zhang

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n-2:
            if nums[i] > 0:
                break
            target = -nums[i]
            low, high = i+1, n-1
            while low < high:
                sums = nums[low] + nums[high]
                left, right = nums[low], nums[high]
                if sums < target:
                    while low < high and nums[low] == left:
                        low += 1
                elif sums > target:
                    while low < high and nums[high] == right:
                        high -= 1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == left:
                        low += 1
                    while low < high and nums[high] == right:
                        high -= 1
            num_i = nums[i]
            while i < n-2 and nums[i] == num_i:
                i += 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums))






