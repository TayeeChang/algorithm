# -*- coding: utf-8 -*-
# @Time : 2021/4/22 15:20
# @Author : haojie zhang

# 接雨水


#单调栈or单调队列
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


# 双指针
def trap_2_points(height):
    if not height:
        return 0
    left, right = 0, len(height)-1
    l_max, r_max = height[0], height[-1]
    res = 0
    while left <= right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        if l_max < r_max:
            res += l_max - height[left]
            left += 1
        else:
            res += r_max - height[right]
            right -= 1
    return res


height = [4, 2, 0, 3, 2, 5]
print(trap(height))