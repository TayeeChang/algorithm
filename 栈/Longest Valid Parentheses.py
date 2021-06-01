# -*- coding: utf-8 -*-
# @Time : 2021/5/20 11:15
# @Author : haojie zhang

"""
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
"""

# 栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        return res


# 动态规划版
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            if s[i-1] == ')':
                if i >= 2 and s[i-2] == '(':
                    dp[i] = dp[i-2] + 2
                elif i >= 2 and s[i-2] == ')':
                    if i-dp[i-1]-2 >= 0 and s[i-dp[i-1]-2] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        return max(dp)

s = ')(())('
obj = Solution1()
print(obj.longestValidParentheses(s))

