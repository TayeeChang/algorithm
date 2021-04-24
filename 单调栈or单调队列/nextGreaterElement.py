# -*- coding: utf-8 -*-
# @Time : 2021/4/22 14:12
# @Author : haojie zhang


def nextGreaterElement(nums):
    if not nums:
        return nums
    n = len(nums)
    stack = []
    res = [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


nums = [1, 3, 2, 5, 4]
res = nextGreaterElement(nums)
print(res)

