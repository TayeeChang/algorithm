# -*- coding: utf-8 -*-
# @Time : 2021/5/26 10:01
# @Author : haojie zhang

"""
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j])  i <= k < j
"""


class Solution:
    def matrix_chain(self, nums):
        n = len(nums) - 1  # 矩阵的数目
        m = [[float('inf')] * n for _ in range(n)]
        s = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 0

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                for k in range(i, j):
                    t = m[i][k] + m[k+1][j] + nums[i] * nums[k+1] * nums[j+1]
                    if t < m[i][j]:
                        m[i][j] = t
                        s[i][j] = k
        return m, s

    def print_parent(self, s, i, j):
        if i == j:
            print('A'+str(i+1), end='')
        else:
            print('(', end='')
            self.print_parent(s, i, s[i][j])
            self.print_parent(s, s[i][j]+1, j)
            print(')', end='')


nums = [30, 35, 15, 5, 10, 20, 25]

obj = Solution()
m, s = obj.matrix_chain(nums)
obj.print_parent(s, 0, len(nums)-2)
print()
print(m[0][-1])
