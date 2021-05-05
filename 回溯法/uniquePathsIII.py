# -*- coding: utf-8 -*-
# @Time : 2021/5/2 13:07
# @Author : haojie zhang

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def traceback(grid, i, j, used, cnt, tmp):
            if grid[i][j] == 2:
                nonlocal res
                nonlocal zero
                if cnt == zero:
                    res += 1
                    ans.append(tmp)
                return
            if grid[i][j] == 0:
                cnt += 1
            for offset_i, offset_j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                tmp_i = i + offset_i
                tmp_j = j + offset_j
                if not isValid(grid, tmp_i, tmp_j, used):
                    continue
                used[tmp_i][tmp_j] = True
                traceback(grid, tmp_i, tmp_j, used, cnt, tmp+[grid[tmp_i][tmp_j]])
                used[tmp_i][tmp_j] = False

        def isValid(grid, i, j, used):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or used[i][j] or grid[i][j] == -1:
                return False
            return True

        res = 0
        ans = []
        m, n = len(grid), len(grid[0])
        used = [[False] * (n) for _ in range(m)]
        zero = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zero += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    used[i][j] = True
                    traceback(grid, i, j, used, 0, [grid[i][j]])
                    used[i][j] = False
        return res


grid = [[1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]]
print(grid)
s = Solution()
print(s.uniquePathsIII(grid)[1])
