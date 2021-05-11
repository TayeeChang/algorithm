# -*- coding: utf-8 -*-
# @Time : 2021/5/11 11:08
# @Author : haojie zhang
"""
845. 数组中的最长山脉
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。
https://leetcode-cn.com/problems/longest-mountain-in-array/
"""

from typing import  List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        # 先确定山顶（当前元素比两边大），然后向两边延伸
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:  # 当前左边界，山顶，右边界的下标
                left, top, right = i - 1, i, i + 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < len(arr) - 1 and arr[right + 1] < arr[right]:
                    right += 1
                res = max(res, right - left + 1)
        return res


    # 动态规划解法
    def longestMountain1(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0] * n  # [0, ..., i)递增的个数
        right = [0] * n  # (i, ..., n-1]递减的个数
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                left[i] = left[i-1] + 1
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                right[i] = right[i+1] + 1
        res = 0
        for i in range(1, n-1):
            if left[i] > 0 and right[i] > 0:
                res = max(res, left[i] + right[i] + 1)
        return res


arr = [2, 1, 4, 7, 3, 2, 5]
s = Solution()
print(s.longestMountain1(arr))





