# -*- coding: utf-8 -*-
# @Time : 2021/5/15 22:46
# @Author : haojie zhang


from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                low, high = j + 1, len(nums) - 1
                while low < high:
                    sums = nums[i] + nums[j] + nums[low] + nums[high]
                    if sums == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:  # low 去重
                            low += 1
                        low += 1
                        while low < high and nums[high] == nums[high - 1]:  # high 去重
                            high -= 1
                        high -= 1
                    elif sums < target:
                        while low < high and nums[low] == nums[low + 1]:  # low去重
                            low += 1
                        low += 1
                    else:
                        while low < high and nums[high] == nums[high - 1]:  # high 去重
                            high -= 1
                        high -= 1
        return res


nums = [-3,-1,0,2,4,5]
target = 2
s = Solution()
print(s.fourSum(nums, target))