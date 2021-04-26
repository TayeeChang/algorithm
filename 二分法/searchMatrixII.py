# -*- coding: utf-8 -*-
# @Time : 2021/4/26 18:14
# @Author : haojie zhang

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if matrix[i][j] < target:
                 i += 1
            elif matrix[i][j] > target:
                 j -= 1
            else:
                return True
        return False


nums = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
print(Solution().searchMatrix(nums, target))


class Solution:
    def searchMatrix(self, matrix, target):
        def binay_search(nums,target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    l = mid + 1
                if nums[mid] > target:
                    r = mid - 1
            return False
        l_l = len(matrix[0])
        l_r = len(matrix)
        # if l_l >= l_r:
        for line in matrix:
            if line[0] <= target and line[l_l - 1] >= target:
                if binay_search(line, target):
                    return True
        return False
        # else:
        #     for i in range(l_l):
        #         if matrix[0][i] <= target and matrix[l_r - 1][i] >= target:
        #             if binay_search([x[i] for x in matrix], target):
        #                 return True
        #     return False
