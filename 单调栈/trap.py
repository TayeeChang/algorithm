# -*- coding: utf-8 -*-
# @Time : 2021/4/22 15:20
# @Author : haojie zhang

# 接雨水


def trap(height):
    stack = []
    res = 0
    for i, num in enumerate(height):
        while stack and stack[-1][1] < num:
            j, curr = stack.pop()
            if stack:
                height = min(stack[-1][1], num) - curr
                width = i - stack[-1][0] - 1
                res += height * width
        stack.append((i, num))
    return res


height = [4, 2, 0, 3, 2, 5]
print(trap(height))