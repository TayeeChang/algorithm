# -*- coding: utf-8 -*-
# @Time : 2021/4/22 16:49
# @Author : haojie zhang


def dailyTemperatures(T):
    n = len(T)
    stack = []
    res = [0] * n
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))
