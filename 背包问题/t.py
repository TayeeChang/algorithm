# -*- coding: utf-8 -*-
# @Time : 2021/5/2 22:35
# @Author : haojie zhang


def help(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

print(help(4))