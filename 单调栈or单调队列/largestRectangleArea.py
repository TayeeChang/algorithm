# -*- coding: utf-8 -*-
# @Time : 2021/4/25 15:20
# @Author : haojie zhang

"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        heights = [0] + heights + [0]  # 哨兵技巧，左0保证所有元素都能入栈，右0保证所有元素都能出栈，最终栈为空
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                while stack and heights[stack[-1]] == heights[j]:
                    stack.pop()
                width = i - stack[-1] - 1
                height = heights[j]
                res = max(res, width * height)
            stack.append(i)
        return res


heights = [0, 2, 0]
print(Solution().largestRectangleArea(heights))



