# -*- coding: utf-8 -*-
# @Time : 2021/5/25 17:15
# @Author : haojie zhang

"""
Q：给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。
注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。
请你计算并返回从数组中删除所有数字所需的最少操作次数。

示例 1：
输入：arr = [1,2]
输出：2
示例 2：
输入：arr = [1,3,4,1,5]
输出：3
解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。

A：
经典的区间dp，我们令f(i,j)f(i,j)代表删除区间[i,j][i,j]的最小值（即最小删除次数），那么可得以下递推公式：


分析一下，这里根据a[i]是否等于a[j]，分两种情况。因为当a[i] = a[j]的时候，有可能产生最小删除次数的方案是a[i]和a[j]等到最后一起被删。
dp[i][j] = min(dp[i][j], dp[i+1][j-1], dp[i][k] + dp[k+1][j])
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
"""

from typing import List
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[n] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                for k in range(i, j):
                    if arr[i] == arr[j]:
                        dp[i][j] = min(dp[i][j], dp[i+1][j-1], dp[i][k] + dp[k+1][j])
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
        return dp[0][-1]


arr = [1, 1, 3, 4, 1, 5, 1]
s = Solution()
print(s.minimumMoves(arr))