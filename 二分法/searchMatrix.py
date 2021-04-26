# -*- coding: utf-8 -*-
# @Time : 2021/4/26 16:26
# @Author : haojie zhang

"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
https://leetcode-cn.com/problems/search-a-2d-matrix/
"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1
        while low <= high:
            mid = low + (high - low) // 2
            i = mid // col
            j = mid % col
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


nums = [[1, 1]]
target = 2
print(Solution().searchMatrix(nums, target))