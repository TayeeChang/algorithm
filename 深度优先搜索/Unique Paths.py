# -*- coding: utf-8 -*-
# @Time : 2021/5/31 15:08
# @Author : haojie zhang

# 时间复杂度为 O(n^4)； 空间复杂度为 O(n)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m < 1 or n < 1:
            return 0
        if m == 1 and n == 1:
            return 1

        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


# 深搜 + 缓存， 即 备忘录方法
# 时间复杂度为 O(n^2)； 空间复杂度为 O(n^2)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(m, n):
            if m < 1 or n < 1:
                return 0
            if m == 1 and n == 1:
                return 1
            if (m, n) in hashMap:
                return hashMap[(m, n)]
            hashMap[(m, n)] = dfs(m - 1, n) + dfs(m, n - 1)
            return hashMap[(m, n)]

        hashMap = {}
        return dfs(m, n)

# 动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]