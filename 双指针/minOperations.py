# -*- coding: utf-8 -*-
# @Time : 2021/5/11 17:34
# @Author : haojie zhang

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        res = -1
        left = right = 0
        sums = 0
        while right < len(nums):
            sums += nums[right]
            right += 1
            while left < right and sums >= target:
                if sums == target:
                    res = max(res, right-left)
                sums -= nums[left]
                left += 1
        return len(nums) - res if res != -1 else -1


nums = [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
x = 134365
s = Solution()
print(s.minOperations(nums, x))
