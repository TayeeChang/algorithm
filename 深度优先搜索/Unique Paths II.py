# -*- coding: utf-8 -*-
# @Time : 2021/5/31 15:24
# @Author : haojie zhang


from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(m, n):
            if obstacleGrid[m-1][n-1] == 1:
                return 0
            if m == 1 and n == 1:
                return 1
            if m < 1 or n < 1:
                return 0

            if (m, n) in hashMap:
                return hashMap[(m, n)]
            hashMap[(m, n)] = dfs(m-1, n) + dfs(m, n-1)
            return hashMap[(m, n)]

        hashMap = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(m, n)
