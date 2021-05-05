# -*- coding: utf-8 -*-
# @Time : 2021/5/4 20:34
# @Author : haojie zhang

"""
1219. 黄金矿工
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：

每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。


示例 1：

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。
https://leetcode-cn.com/problems/path-with-maximum-gold/
"""

from typing import List


# 版本一
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def can_be_start(grid, i, j):
            if not grid[i][j]:
                return False
            cnt = 0
            for offset_i, offset_j in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                new_i = i + offset_i
                new_j = j + offset_j
                if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]:
                    cnt += 1
            if cnt <= 2:
                return True
            return False

        def traceback(grid, row, col, tmp):
            nonlocal res
            res = max(res, tmp)
            for offset_row, offset_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_row = row + offset_row
                new_col = col + offset_col

                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                if not grid[new_row][new_col]:
                    continue
                v = grid[new_row][new_col]
                grid[new_row][new_col] -= v
                traceback(grid, new_row, new_col, tmp + v)
                grid[new_row][new_col] = v

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if can_be_start(grid, i, j):
                    tmp = grid[i][j]
                    grid[i][j] = 0
                    traceback(grid, i, j, tmp)
                    grid[i][j] = tmp
        return res


# 版本二
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def can_be_start(grid, i, j):
            if not grid[i][j]:
                return False
            cnt = 0
            for offset_i, offset_j in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                new_i = i + offset_i
                new_j = j + offset_j
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j]:
                    cnt += 1
            if cnt <= 2:
                return True
            return False

        def traceback(grid, row, col, tmp):
            nonlocal res
            res = max(res, tmp)
            t = grid[row][col]
            grid[row][col] = 0
            for offset_row, offset_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_row = row + offset_row
                new_col = col + offset_col

                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                if not grid[new_row][new_col]:
                    continue
                traceback(grid, new_row, new_col, tmp + grid[new_row][new_col])
            grid[row][col] = t

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if can_be_start(grid, i, j):
                    traceback(grid, i, j, grid[i][j])

        return res


grid = [
        [0, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
]

s = Solution()
print(s.getMaximumGold(grid))