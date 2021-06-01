# -*- coding: utf-8 -*-
# @Time : 2021/5/24 16:28
# @Author : haojie zhang

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not  matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights):

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


matrix = [["1","0"]]
s = Solution()
print(s.maximalRectangle(matrix))



