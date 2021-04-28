# -*- coding: utf-8 -*-
# @Time : 2021/4/28 14:02
# @Author : haojie zhang

"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)

        k = (m + n + 1) // 2
        low, high = 0, m

        while low < high:
            i = low + (high - low) // 2  # 短数组分割线右边第一个数下标
            j = k - i                    # 长数组分割线右边第一个数下标
            if nums1[i] <= nums2[j-1]:
                low = i + 1
            else:
                high = i

        i = low
        j = k - i

        leftMax1 = float('-inf') if i == 0 else nums1[i-1]
        leftMax2 = float('-inf') if j == 0 else nums2[j - 1]

        rightMin1 = float('inf') if i == m else nums1[i]
        rightMin2 = float('inf') if j == n else nums2[j]

        if (m+n) % 2 == 1:
            return max(leftMax1, leftMax2)

        return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2


nums1 = [3]
nums2 = [-2, -1]

print(Solution().findMedianSortedArrays(nums1, nums2))

