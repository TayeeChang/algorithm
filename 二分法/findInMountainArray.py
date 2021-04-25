# -*- coding: utf-8 -*-
# @Time : 2021/4/25 16:57
# @Author : haojie zhang

"""
1095. 山脉数组中查找目标值
（这是一个 交互式问题 ）

给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

如果不存在这样的下标 index，就请返回 -1。



何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

首先，A.length >= 3

其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
https://leetcode-cn.com/problems/find-in-mountain-array/
"""


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        low, high = 0, n-1
        while low < high:
            mid = low + (high - low) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                low = mid + 1
            else:
                high = mid

        middle = low
        low, high = 0, middle

        while low < high:
            mid = low + (high-low) // 2
            if mountain_arr.get(mid) < target:
                low = mid + 1
            elif mountain_arr.get(mid) > target:
                high = mid
            else:
                return mid
        low, high = middle, n

        while low < high:
            mid = low + (high-low) // 2
            if mountain_arr.get(mid) < target:
                high = mid
            elif mountain_arr.get(mid) > target:
                low = mid + 1
            else:
                return mid
        return -1





