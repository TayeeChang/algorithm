# -*- coding: utf-8 -*-
# @Time : 2021/5/21 16:09
# @Author : haojie zhang

"""
120. 三角形最小路径和
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
https://leetcode-cn.com/problems/triangle/
"""

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        return triangle[0][0]



triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
s = Solution()
print(s.minimumTotal(triangle))