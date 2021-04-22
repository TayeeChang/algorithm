# -*- coding: utf-8 -*-
# @Time : 2021/4/22 18:07
# @Author : haojie zhang

import heapq


class Solution:
    def trapRainWater(self, heightMap) -> int:
        row, col = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        # 行
        for i in range(row):
            heapq.heappush(heap, [heightMap[i][0], i, 0])
            heapq.heappush(heap, [heightMap[i][col - 1], i, col - 1])
            visited.add((i, 0))
            visited.add((i, col - 1))
        # 列
        for j in range(col):
            heapq.heappush(heap, [heightMap[0][j], 0, j])
            heapq.heappush(heap, [heightMap[row - 1][j], row - 1, j])
            visited.add((0, j))
            visited.add((row - 1, j))

        curr = float('-inf')
        res = 0
        while heap:
            num, i, j = heapq.heappop(heap)
            curr = max(curr, num)
            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                tmp_i = i + x
                tmp_j = j + y
                if tmp_i < 0 or tmp_i >= row or tmp_j < 0 or tmp_j >= col or (tmp_i, tmp_j) in visited:
                    continue
                visited.add((tmp_i, tmp_j))
                if heightMap[tmp_i][tmp_j] < curr:
                    res += curr - heightMap[tmp_i][tmp_j]

                heapq.heappush(heap, [heightMap[tmp_i][tmp_j], tmp_i, tmp_j])
        return res


nums = \
[
  [1, 4, 3, 1, 3, 2],
  [3, 2, 1, 3, 2, 4],
  [2, 3, 3, 2, 3, 1]
]
s = Solution()
print(s.trapRainWater(nums))


