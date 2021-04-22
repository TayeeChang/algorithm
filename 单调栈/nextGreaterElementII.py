# -*- coding: utf-8 -*-
# @Time : 2021/4/22 14:43
# @Author : haojie zhang


def nextGreaterElement(nums):
    n = len(nums)
    res = [-1] * n
    nums += nums
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            res[index] = nums[i]
        stack.append(i % n)
    return res


nums = [1, 2, 1]
print(nextGreaterElement(nums))

