# -*- coding: utf-8 -*-
# @Time : 2021/6/1 17:32
# @Author : haojie zhang


"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
https://leetcode-cn.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                res = max(res, height[left] * (right-left))
                left += 1
            else:
                res = max(res, height[right] * (right-left))
                right -= 1
        return res
