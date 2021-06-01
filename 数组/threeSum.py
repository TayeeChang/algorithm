# -*- coding: utf-8 -*-
# @Time : 2021/5/15 22:19
# @Author : haojie zhang


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:  # 第一个元素去重
                continue
            low, high = i+1, len(nums)-1
            while low < high:
                sums = nums[i] + nums[low] + nums[high]
                if sums == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:  # low 去重
                        low += 1
                    low += 1
                    while low < high and nums[high] == nums[high-1]:  # high 去重
                        high -= 1
                    high -= 1
                elif sums < 0:
                    while low < high and nums[low] == nums[low+1]:  # low去重
                        low += 1
                    low += 1
                else:
                    while low < high and nums[high] == nums[high-1]:  # high 去重
                        high -= 1
                    high -= 1
        return res


nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))

