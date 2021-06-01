# -*- coding: utf-8 -*-
# @Time : 2021/5/20 14:37
# @Author : haojie zhang

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack[-1]]
                stack.pop()
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)

        return res


heights = [2,1,5,6,2,3]
s = Solution()
print(s.largestRectangleArea(heights))
