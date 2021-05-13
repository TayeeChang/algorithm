# -*- coding: utf-8 -*-
# @Time : 2021/4/27 14:24
# @Author : haojie zhang

"""
前缀和
--------适用于 区间求和 及 连续子数组 等类似问题。
"""

"""
724. 寻找数组的中心下标
给你一个整数数组 nums，请编写一个能够返回数组 “中心下标” 的方法。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心下标，返回 -1 。如果数组有多个中心下标，应该返回最靠近左边的那一个。

注意：中心下标可能出现在数组的两端。
https://leetcode-cn.com/problems/find-pivot-index/
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]

        for i in range(n):
            if 2 * preSum[i] + nums[i] == preSum[-1]:
                return i
        return -1