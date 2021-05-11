# -*- coding: utf-8 -*-
# @Time : 2021/5/11 17:14
# @Author : haojie zhang

"""
1004. 最大连续1的个数 III
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。



示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。

https://leetcode-cn.com/problems/max-consecutive-ones-iii/
"""


from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        res = 0
        left = right = 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            right += 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            res = max(res, right - left)
        return res


