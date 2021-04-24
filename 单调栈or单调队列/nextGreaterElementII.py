# -*- coding: utf-8 -*-
# @Time : 2021/4/22 14:43
# @Author : haojie zhang


def nextGreaterElement(nums):
    """
    环形数组通常使用的是将数组长度翻倍，然后使用求模运算（%）技巧
    """
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2*n):
        while stack and nums[stack[-1]] < nums[i % n]:
            index = stack.pop()
            res[index] = nums[i % n]
        stack.append(i % n)
    return res


nums = [1, 2, 1]
print(nextGreaterElement(nums))


