# -*- coding: utf-8 -*-
# @Time : 2021/5/10 16:33
# @Author : haojie zhang

"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        res = float('inf')
        sums = 0
        while right < len(nums):
            sums += nums[right]
            right += 1
            while sums >= target:
                res = min(res, right - left)
                sums -= nums[left]
                left += 1

        return res if res != float('inf') else 0


target = 7
nums = [2,3,1,2,4,3]
s = Solution()
print(s.minSubArrayLen(target, nums))